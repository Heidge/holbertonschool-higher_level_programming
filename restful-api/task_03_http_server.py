import http.server
import socketserver
import json

PORT = 8000
DATA = {"name": "John", "age": 30, "city": "New York"}
INFOS = {"version": "1.0", "description": "A simple API built with http.server"}

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            json_data = bytes(json.dumps(DATA), "utf-8")
            self.wfile.write(json_data)
        elif self.path == "/status":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == "/infos":
            self.send_response(200)
            self.end_headers()
            json_infos = bytes(json.dumps(INFOS), "utf-8")
            self.wfile.write(json_infos)
        elif self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"This is a simple API")
        else:
            self.send_error(404, "Endpoint not found", None)
            self.end_headers()


with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
