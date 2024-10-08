import http.server
import socketserver
import json

PORT = 8000
DATA = {"name": "John", "age": 30, "city": "New York"}
INFOS = {"version": "1.0", "description": "A simple API built with http.server"}

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    Create a simple HTTP request handler

    Args:
        http (BaseHTTPRequestHandler): Parent of our class for get his methods and attributes
    """
    def do_GET(self):
        """
        Function for manage routes
        """
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
        elif self.path == "/info":
            self.send_response(200)
            self.end_headers()
            json_infos = bytes(json.dumps(INFOS), "utf-8")
            #On encode en bytes car la méthode write en dessous veut du binaire
            self.wfile.write(json_infos)
        elif self.path == "/":
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        else:
            self.send_response(404, "Endpoint not found")
            self.end_headers()
            self.wfile.write(b'404 Not Found')


with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
