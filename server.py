from http.server import HTTPServer, BaseHTTPRequestHandler


def read_file():
    f = open("content.txt", "r")
    return f.read()


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(read_file().encode("cp1251"))


httpd = HTTPServer(("localhost", 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()
