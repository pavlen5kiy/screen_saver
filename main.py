# import required modules
import http.server
import socketserver
import json


# define a handler to serve the HTML page
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # serve the HTML page
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)


# set up the HTTP server
handler_object = MyHttpRequestHandler
PORT = 8080
my_server = socketserver.TCPServer(("", PORT), handler_object)

# start the server
print("Server started at localhost:" + str(PORT))
my_server.serve_forever()
