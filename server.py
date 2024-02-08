from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 8000

Handler = SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
