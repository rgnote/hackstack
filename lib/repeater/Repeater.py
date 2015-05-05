__author__ = 'rakesh'


import os
import threading
import requests


class Repeater(threading.Thread):

    def __init__(self, url, method, body, headers, resreq, resres, rescook, resview):
        threading.Thread.__init__(self)
        self.url = url
        self.method = method
        self.body = body
        self.headers = headers
        self.resreq = resreq
        self.resres = resres
        self.rescook = rescook
        self.resview = resview


    def run(self):
        print "asdf"
        if self.method.lower() == "get":
            req = requests.get(url=self.url, headers=self.headers,verify=False)
        else:
            req = requests.get(url=self.url, data=self.body, headers=self.headers,verify=False)

        reqcontent = ""
        for i in self.headers:
            reqcontent += str(i)+" : "+str(self.headers[i])+"\n"


        rescontent = ""
        for i in req.headers:
            rescontent += str(i)+" : "+str(req.headers[i])+"\n"

        cookcontent = ""
        # for i in req.cookies:
        #     cookcontent += str(i)+" : "+str(req.cookies[i])+"\n"
        if cookcontent == "":
            cookcontent = "No cookies!"

        self.resreq.append(reqcontent)
        self.resres.insertPlainText(rescontent+"\n\n"+req.content)
        self.rescook.insertPlainText(cookcontent)
        self.resview.insertHtml(req.content)


