#!/bin/bash
# Double-click to serve the weather dashboard locally so geolocation works.
cd "$(dirname "$0")"
PORT=8080
URL="http://localhost:$PORT"
echo "Serving weather dashboard at $URL  (press Ctrl+C to stop)"
( sleep 1; open "$URL" ) >/dev/null 2>&1 &
# Serve with no-store headers so edits always show up on reload (no stale cache).
python3 - "$PORT" <<'PY'
import sys, http.server, socketserver
class H(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store, must-revalidate")
        self.send_header("Pragma", "no-cache")
        super().end_headers()
with socketserver.TCPServer(("", int(sys.argv[1])), H) as httpd:
    httpd.serve_forever()
PY
