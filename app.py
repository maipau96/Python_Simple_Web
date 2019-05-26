import http.server as server
import SocketServer

PORT = 8000

Handler = server.SimpleHTTPRequestHandler


httpd = SocketServer.TCPServer(("", PORT), Handler)

print ("Serving at port", PORT)
httpd.serve_forever()

#search for IP address. open terminal and type: ipconfig
#server command: python -m http.server 8000 --bind 192.168.0.104
