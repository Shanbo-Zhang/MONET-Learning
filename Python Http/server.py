import http.server
from datetime import datetime

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/time":
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(f"{current_time}".encode())
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"File ^_^")
    
http.server.HTTPServer(('', 1234), RequestHandler).serve_forever()