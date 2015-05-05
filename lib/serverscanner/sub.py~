from subprocess import Popen, PIPE
from time import sleep
from nbstreamreader import NonBlockingStreamReader as NBSR

# run the shell as a subprocess:
p = Popen(['perl','nikto.pl','-host','127.0.0.1'],
        stdin = None, stdout = PIPE, stderr = None, shell = False)
# wrap p.stdout with a NonBlockingStreamReader object:
nbsr = NBSR(p.stdout)
# issue command:
# get the output
while True:
    output = nbsr.readline(1)
    # 0.1 secs to let the shell output the result
    if output != None:
        print output,
    elif "End Time" in str(output):
    	break
