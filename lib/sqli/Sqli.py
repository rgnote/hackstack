__author__ = 'rakesh'

import os
import time
from subprocess import Popen, PIPE
from threading import Thread


class SQLI(Thread):

    def __init__(self, cmd, tb):
        Thread.__init__(self)
        self.cmd = cmd
        self.tb = tb

    def run(self):
        print "SQL injector started"
        self.tb.append("SQL injector started\n")
        currentdir = os.getcwd()
        os.chdir('./lib/sqli/')
        cmdlist = ['python', 'sqlmap.py']
        for i in self.cmd.split(" "):
            cmdlist.append(i)
        print cmdlist
        p = Popen(cmdlist, stdin=None, stdout=PIPE, stderr=None, shell=False)
        while True:
            time.sleep(0.01)
            outdata = p.stdout.readline()
            if not outdata and p.returncode is not None:
                break
            self.tb.append(outdata)
            p.poll()
        os.chdir(currentdir)