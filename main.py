from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

def run(server_class=HTTPServer,
        handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        with open("song.mp3", "rb") as songFile:
            songStream = songFile.read()
            # while byte != "":
            #     songStream.append(byte)
            #     byte += songFile.read(1)
            #     songStream.append(byte)

            self.send_response(200)
            self.send_header('Content-type','audio/mpeg')
            self.end_headers()
            self.wfile.write(songStream)

run(HTTPServer, handler)