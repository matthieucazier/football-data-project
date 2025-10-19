from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import os

PORT = 8000
web_dir = os.path.join(os.path.dirname(__file__))
os.chdir(web_dir)

Handler = SimpleHTTPRequestHandler
with TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
