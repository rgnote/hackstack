import multiprocessing.forking

__author__ = 'rakesh'


import os
import threading
from subprocess import Popen, PIPE


class PortScan(threading.Thread):

    def __init__(self, ip, port, tb):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.tb = tb

    def run(self):
            currentdir = os.getcwd()
            os.chdir('./lib/portscanner/')
            p = Popen(["python", "Scan.py", self.ip, self.port], stdout=PIPE)
            while True:
                outdata = p.stdout.readline()
                if not outdata and p.returncode is not None:
                    break
                self.tb.append(outdata)
                p.poll()
            os.chdir(currentdir)