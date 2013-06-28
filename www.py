#!/usr/bin/env python
import SimpleHTTPServer
import SocketServer

print "Welcome to kuangl's Web Server"
PORT = 880
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "services start at port", PORT
httpd.serve_forever()
