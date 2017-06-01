# import socketserver, ssl, time, os

# class MyHTTPSHandler_socket(socketserver.BaseRequestHandler):
    
#     def handle(self):
        
#         context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
#         context.load_cert_chain(certfile=(script_home+'/Cert/server.crt'), keyfile=(script_home+'/Cert/server.key'))
#         SSLSocket = context.wrap_socket(self.request, server_side=True)
#         self.data = SSLSocket.recv(2048)
#         print(self.data)
#         buf = 'test HTTPS Server Handler<br>%f'%time.time()
#         buf = buf.encode()
#         SSLSocket.send(buf)

# script_home = os.path.dirname(os.path.abspath(__file__))  
# if __name__ == "__main__":
#     port = 443
#     httpd = socketserver.TCPServer(('0.0.0.0', port), MyHTTPSHandler_socket)
#     # httpd.socket = ssl.wrap_socket(httpd.socket, certfile=(script_home+'/Cert/server.crt'), keyfile=(script_home+'/Cert/server.key'), server_side=True)  
#     print('https serving at port', port)
#     httpd.serve_forever()



# from http.server import HTTPServer,BaseHTTPRequestHandler,SimpleHTTPRequestHandler 
# # import BaseHTTPServer  
# # import SimpleHTTPServer  
# import os  
# import socket  
# import ssl  
  
# script_home = os.path.dirname(os.path.abspath(__file__))  
# # ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) \  
# #       for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]  
# ip = "xiaoyue34561.vicp.net"
# port = 443  
  
# class MyHTTPRequestHandler(BaseHTTPRequestHandler):
#     server_version = "SimpleHTTP/"

#     # def handle(self):
#     #     print("handle")
#     def do_GET(self):
#         print("get")
#         """Serve a GET request."""
#         self.send_response(200)
#         return "OK"

# def main():  
#     print ("simple https server, address:%s:%d, document root:%s" % (ip, port, script_home))  
  
#     httpsd = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)  
#     httpsd.socket = ssl.wrap_socket(httpsd.socket, certfile=(script_home+'/Cert/server.crt'), keyfile=(script_home+'/Cert/server.key'), server_side=True)  
#     httpsd.serve_forever()  


#     httpd = HTTPServer(('0.0.0.0', 80), MyHTTPRequestHandler)  
#     httpd.serve_forever() 
  
# if __name__ == '__main__':  
#     os.chdir(script_home)  
#     main()  










# import HTTPServer,BaseHTTPRequestHandler,SimpleHTTPRequestHandler 
import BaseHTTPServer  
import SimpleHTTPServer  
import os  
import socket  
import ssl  
  
script_home = os.path.dirname(os.path.abspath(__file__))  
# ip = [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) \  
#       for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]  
ip = "xiaoyue34561.vicp.net"
port = 443  
  
# class MyHTTPRequestHandler(BaseHTTPRequestHandler):
#     server_version = "SimpleHTTP/"

#     # def handle(self):
#     #     print("handle")
#     def do_GET(self):
#         print("get")
#         """Serve a GET request."""
#         self.send_response(200)
#         return "OK"

def main():  
    print ("simple https server, address:%s:%d, document root:%s" % (ip, port, script_home))  
  
    httpsd = BaseHTTPServer.HTTPServer(('0.0.0.0', port), SimpleHTTPServer.SimpleHTTPRequestHandler)  
    httpsd.socket = ssl.wrap_socket(httpsd.socket, certfile=(script_home+'/Cert/server.crt'), keyfile=(script_home+'/Cert/server.key'), server_side=True)  
    httpsd.serve_forever()  


    httpd = HTTPServer(('0.0.0.0', 80), MyHTTPRequestHandler)  
    httpd.serve_forever() 
  
if __name__ == '__main__':  
    os.chdir(script_home)  
    main()  