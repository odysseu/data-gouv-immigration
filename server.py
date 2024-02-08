from http.server import SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import socketserver
from app.render.renderTable import render_table, render_graphics

PORT = 8000


class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)

        if parsed_url.path == '/api/render':
            content_type = query_params.get('type', [''])[0]
            if content_type == 'table':
                content = render_table()
            elif content_type == 'graphics':
                content = render_graphics()
            else:
                content = ''

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(content.encode())

        else:
            super().do_GET()


Handler = MyHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()
