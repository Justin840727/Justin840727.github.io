import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("18.85.25.110", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()