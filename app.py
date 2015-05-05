#!/usr/bin/python
__author__ = 'rakesh'
# PySide Modules
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtWebKit import *


# Standard library modules
import sys
import time
import string

# third party modules

# Core Functionality modules
from lib.portscanner.PortScanner import PortScan
from lib.serverscanner.ServerScanner import ServerScan
from lib.repeater.Repeater import Repeater
from lib.sqli.Sqli import SQLI
from lib.encoder.encoder import Encoder
from lib.exp.exp import Exp
from lib.shell.shell import Shell


# User Interface Modules
from ui import WindowGui
from ui import splash
from ui import About


class AboutDialog(QDialog, About.Ui_Dialog):

    def __init__(self, parent=None):
        super(AboutDialog, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QMainWindow, WindowGui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # Browser functionality  /Adding View to browser tab
        self.view = QWebView()
        self.browserbodylayout.addWidget(self.view)
        self.view.setStyleSheet("background-color:#FFFFFF;")
        self.browserseturl("http://10.10.2.53")
        self.view.show()
        # Connecting signals and slots
        # PortScanner
        self.portscannerstart.clicked.connect(self.portscannermethod)

        # ServerScanner
        self.serverscannerstart.clicked.connect(self.serverscannermethod)

        # Repeater
        self.repeatersend.clicked.connect(self.repeatermethod)

        # SQLI
        self.sqlistart.clicked.connect(self.sqlimethod)

        # EnDecoder
        self.encoderstart.currentIndexChanged.connect(self.encodermethod)

        # Shell
        self.shellstart.clicked.connect(self.shellmethod)

        # Browser
        self.browseraddress.returnPressed.connect(self.browseraddresschanged)
        self.browsergoback.pressed.connect(self.view.back)
        self.browsergofront.pressed.connect(self.view.forward)
        self.browserreload.pressed.connect(self.view.reload)
        self.view.urlChanged.connect(self.browserurlchanged)

        # Online Exploit finder
        self.expstart.clicked.connect(self.expmethod)

        # Menu
        self.actionExit.activated.connect(self.exitapp)
        self.actionAbout.activated.connect(self.showabout)

    def showabout(self):
        self.about = AboutDialog()
        self.about.show()

    def exitapp(self):
        self.destroy()

    # PortScanner slots

    def portscannermethod(self):
        serverip = str(self.portscannerip.text())
        portrange = str(self.portscannerport.text())
        if serverip != "" and portrange != "":
            if len(serverip.split(".")) == 4:
                if portrange is not None:
                    ps = PortScan(serverip, portrange, self.portscannerconsole)
                    ps.start()
                    print("terminated")
                else:
                    self.portscannerconsole.append("\
                        <font color=red>Inputs are invalid </font>")
            else:
                self.portscannerconsole.append("\
                    <font color=red>Inputs are invalid </font>")

    # ServerScanner slots
    def serverscannermethod(self):
        # self.serverscannerconsole.append(str(self.serverscannerip.text())+":"+str(self.serverscannerport.text()))
        serverip = str(self.serverscannerip.text())
        port = str(self.serverscannerport.text())
        if serverip != "" and port != "":
            if len(serverip.split(".")) == 4 and (int(port) % 2 == 0 or int(port) % 2 == 1) and not int(port) < 0:
                proc = ServerScan(serverip, port, self.serverscannerconsole)
                proc.start()
            else:
                self.serverscannerconsole.append(
                    "<font color=red>Inputs are invalid </font>")

    def browserurlchanged(self, url):
        self.browseraddress.setText(url.toString())

    def browserseturl(self, url):
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.browseraddress.setText(url)
        self.view.load(QUrl(url))

    def browseraddresschanged(self):
        url = self.browseraddress.text()
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "http://" + url
        self.view.load(QUrl(url))

    def browsertogglereload(self, val):
        pass

    # Repeater methods

    def repeatermethod(self):
        headeredit = self.repeaterheaderbody.toPlainText().split('\n')
        url = self.repeaterurledit.text()
        headers = {}
        location = headeredit[0]
        method = "get"
        if location.startswith("post") or location.startswith("POST"):
            method = "post"
        url += location.split(" ")[1]
        body = {}
        for headerid in range(1,len(headeredit)):
            if headeredit[headerid] == "":
                for i in headeredit[headerid+1].split("&"):
                    body[i.split('=')[0]] = i.split('=')[1]
                break
            if ':' in headeredit[headerid]:
                rig = headeredit[headerid].split(":")[0]
                lef = "".join(headeredit[headerid].split(":")[1:])
                headers[rig] = lef
        self.repeaterresponcereq.clear()
        self.repeaterresponceres.clear()
        self.repeaterresponcecookies.clear()
        self.repeaterresponceview.clear()
        repeater = Repeater(url, method, body, headers, self.repeaterresponcereq, self.repeaterresponceres, self.repeaterresponcecookies, self.repeaterresponceview)
        repeater.start()

    def sqlimethod(self):
        cmd = str(self.sqliedit.text())
        if cmd != "":
            proc = SQLI(cmd, self.sqlitb)
            proc.start()
        else:
            self.sqlitb.append("<font color=red>Inputs are invalid </font>")

    def encodermethod(self,val):
        inp = self.encoderinput.toPlainText()
        out = self.encoderoutput
        self.encoderoutput.clear()
        coder = Encoder(inp, out, val)
        coder.start()

    def expmethod(self):
        inp = self.expedit.text()
        out = self.exptb
        self.exptb.clear()
        exp = Exp(inp,out)
        exp.start()

    def shellmethod(self):
        shell = Shell()
        shell.start()


class SplashScreen(QDialog, splash.Ui_Dialog):

    def __init__(self, parent=None):
        super(SplashScreen, self).__init__(parent)
        self.setupUi(self)
        self.label = QLabel("Loading")
        self.setWindowFlags(Qt.SplashScreen)


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        splashscreen = SplashScreen()
        splashscreen.show()
        splashscreen.progressbar.setValue(0)
        value = 0
        while value <= 100:
            time.sleep(0.1)
            value += 9
            splashscreen.progressbar.setValue(value)
        splashscreen.destroy()
        window = MainWindow()
        window.show()
        app.exec_()
    except:
        app.exit()