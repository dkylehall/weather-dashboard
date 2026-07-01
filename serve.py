#!/usr/bin/env python3
"""Static file server for the weather dashboard.

Serves the current directory with no-store headers so edits always show up on a
plain reload. Used by pm2 (see ~/Projects/dev-servers.config.cjs) and can also be
run directly:  python3 serve.py [port]   (default port 8080).
"""
import sys
import http.server

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        super().end_headers()


# ThreadingHTTPServer: one slow/stuck client can't block the others.
http.server.ThreadingHTTPServer.allow_reuse_address = True
with http.server.ThreadingHTTPServer(("", PORT), Handler) as httpd:
    print(f"Serving weather dashboard on http://localhost:{PORT}")
    httpd.serve_forever()
