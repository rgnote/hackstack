__author__ = 'rakesh'

import os
from subprocess import Popen, PIPE
from threading import Thread


class ServerScan(Thread):

    def __init__(self,ip,port,tb):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.tb = tb
    def run(self):
        self.tb.append("server scanner started")
        currentdir=os.getcwd()
        os.chdir('./lib/serverscanner/')
        p = Popen(['perl','nikto.pl','-host',self.ip,'-port',self.port],stdin = None, stdout = PIPE, stderr = None, shell = False)
        while True:
            outdata = p.stdout.readline()
            if not outdata and p.returncode is not None:
                break
            self.tb.append(outdata)
            p.poll()
        os.chdir(currentdir)