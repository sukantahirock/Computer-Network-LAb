# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 22:53:18 2023

@author: USER
"""

import http.server
import socketserver

# Set the directory from which to serve files
directory = "C:/Users/USER/.spyder-py3"  # Set the server's IP address and port
ip = '127.0.0.1'
port = 8000

# Create a custom HTTP request handler
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to allow cross-origin requests (CORS)
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

# Create the HTTP server with your custom handler
with socketserver.TCPServer((ip, port), MyHandler) as httpd:
    print(f"Serving at http://{ip}:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
