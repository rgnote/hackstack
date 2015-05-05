__author__='rakesh'

import threading
import base64
import HTMLParser
import hashlib
import urllib2

class Encoder(threading.Thread):

	def __init__(self, inp, out, val):
		threading.Thread.__init__(self)

		self.inp = inp
		self.out = out
		self.val = val

	def run(self):
		# self.out.append("asdf")
		outputvalue = ""
		if self.val == 1:
			try:
				outputvalue = base64.encodestring(self.inp)
			except:
				outputvalue = "Incorrect padding"
		elif self.val == 2:
			try:
				outputvalue = base64.decodestring(self.inp)
			except:
				outputvalue = "Incorrect padding"
		elif self.val == 3:
			outputvalue = HTMLParser.HTMLParser().unescape(self.inp)
		elif self.val == 4:
			outputvalue = HTMLParser.HTMLParser().unescape(self.inp)
		elif self.val == 5:
			outputvalue = hashlib.md5(self.inp).hexdigest()
		elif self.val == 6:
			outputvalue = hashlib.sha1(self.inp).hexdigest()
		elif self.val == 7:
			outputvalue = urllib2.quote(self.inp.encode("utf8"))
		elif self.val == 8:
			outputvalue = urllib2.unquote(self.inp.encode("utf8"))
		self.out.insertPlainText(outputvalue)