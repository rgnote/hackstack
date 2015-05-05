__author__='rakesh'

import sys
import socket


ip=sys.argv[1]
port=sys.argv[2]


#TODO test portrange for -ve numbers and portrange shud contain only one "-" that too in the middle of ports

if "-" in port:
        start,end = port.split("-")
        start = int(start)
        end = int(end)
else:
    start = end = int(port)

if start>=0 and end<=65535:
	print """
	Starting Port Scanner....
	IP      :   """ + str(ip) + """
	PORT    :   """ + str(port) + """
	"""


	botsocket = socket.socket()
	print "\tPort \tStatus"
	for i in xrange(start,end+1):
	    try:
	        botsocket.connect((ip,i))
	        print "\t%s\t%s" % (i, "Open")
	    except IOError:
		    pass
		    #print str(i)+" Closed"
	        #print "\t%s\t%s" % (i, "Closed")
else:
	print "<font color=red>Inputs Are Invalid</font>"
