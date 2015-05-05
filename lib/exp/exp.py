
import threading
import requests
from bs4 import BeautifulSoup as bs
import time
URL = "https://www.exploit-db.com/search/?action=search&description="

class Exp(threading.Thread):

	def __init__(self, inp, out):
		threading.Thread.__init__(self)
		self.inp = inp
		self.out = out

	def run(self):
		self.out.append("Working..Please wait\n")
		try:
			headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:34.0) Gecko/20100101 Firefox/34.0"}
			req = requests.get(URL+self.inp, headers=headers, verify=False)
			soup = bs(req.content)
			noitems = soup.findAll(class_="pagination")[0].div.text.strip()
			self.out.insertHtml("<font color='green' size='4'>"+noitems+"</font><br><br>")
			exps = soup.find(class_="exploit_list bootstrap-wrapper")
			cont = "<table><thead><tr>" \
			       "<td>Date</td>" \
			       "<td>Download<td>" \
			       "<td>App<td>" \
			       "<td>Verified<td>" \
			       "<td>Description<td>" \
			       "<td>Platform<td>" \
			       "</tr></thead><tbody>"
			# self.out.append(cont)
			for i in exps.findAll(" tr")[1:]:
				da = i.findAll(class_="date")[0].text
				dlink = i.find(class_="dlink").a['href']
				app = i.find(class_="app").text
				verified = i.find(class_="verification").text
				des = i.find(class_="description").a
				platform = i.find(class_="platform").a
				hi = "<tr><td>"+str(da)+"</td><td>"+str(dlink)+"</td><td>"+str(app)+"</td><td>"+str(verified)+"</td><td>"+str(des)+"</td><td>"+str(platform)+"</td></tr>"
				time.sleep(0.1)
				# self.out.append(hi)
			# self.out.append("</tbody></table>")

		except Exception, e:
			print e
			self.out.insertHtml("<br>Something went wrong.<br><font size='3' color='red'>Check your Internet connectivity.</font>")