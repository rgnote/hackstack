import multiprocessing.forking

__author__ = 'rakesh'


import os
import threading
from subprocess import Popen, PIPE


class Shell(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
            Popen(["xterm"])