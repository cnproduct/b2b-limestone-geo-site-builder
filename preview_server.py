#!/usr/bin/env python3
"""
Tianya Limestone Local Preview Server
Serves the compiled 1:1 architectural limestone portal at http://localhost:8080
"""

import http.server
import socketserver
import os
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        # Enable CORS and caching headers
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, must-revalidate')
        super().end_headers()

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        print(f"==================================================")
        print(f"🏛️ Tianya Limestone Portal Preview Server")
        print(f"🌐 Running locally at: http://localhost:{PORT}/")
        print(f"📂 Serving root: {DIRECTORY}")
        print(f"👉 Limestone Hub: http://localhost:{PORT}/index.html")
        print(f"👉 Companion Categories: http://localhost:{PORT}/stone-flooring/other-categories/index.html")
        print(f"👉 Press Ctrl+C to terminate the server.")
        print(f"==================================================")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down preview server.")

if __name__ == '__main__':
    run_server()
