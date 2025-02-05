from http.server import SimpleHTTPRequestHandler
import socketserver

PORT = 8080

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Custom-Header", "Hello from Docker!")
        super().end_headers()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Servidor rodando na porta {PORT}")
    httpd.serve_forever()