#!/usr/local/bin/python3.8

"""
License: MIT License
Copyright (c) 2023 Miel Donkers
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging

import util

class ToolsHandler(BaseHTTPRequestHandler):
    def _set_response(self, code, contentType):
        self.send_response(code)
        self.send_header('Content-type', contentType);
        #self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))

        if(self.path == '/regen'):
            util.genTargetInput()
            self._set_response(200, 'text/plain')
        elif self.path.endswith('.html'):
            with open('.' + self.path, 'r') as f:
                get_html = f.read()
            self._set_response(200, 'text/html')
            self.wfile.write(bytes(get_html, 'utf-8'))
        elif self.path.endswith('.css'):
            with open('.' + self.path, 'r') as f:
                get_html = f.read()
            self._set_response(200, 'text/css')
            self.wfile.write(bytes(get_html, 'utf-8'))
        elif self.path.endswith('.js'):
            with open('.' + self.path, 'r') as f:
                get_html = f.read()
            self._set_response(200, 'text/javascript')
            self.wfile.write(bytes(get_html, 'utf-8'))
        elif self.path.endswith('.json'):
            with open('.' + self.path, 'r') as f:
                get_json = f.read()
            self._set_response(200, 'application/json')
            self.wfile.write(bytes(get_json, 'utf-8'))
        else:
            self._set_response(404, 'text/html')

        #self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=ToolsHandler, host='', port=80):
    logging.basicConfig(level=logging.INFO)
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 3:
        run(host=argv[1], port=int(argv[2]))
    else:
        run()
