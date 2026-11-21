"""
MediMate — IoT Smart Medicine Box & Health Companion Prototype Server
Auto-launches in your web browser at http://localhost:8080
"""
import http.server
import socketserver
import os
import sys
import webbrowser
import threading
import time

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def open_browser():
    time.sleep(0.8)
    webbrowser.open(f"http://localhost:{PORT}")

if __name__ == "__main__":
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("=======================================================================")
            print(f"  MediMate IoT Smart Medicine Box & Health Prototype is LIVE!")
            print(f"  Web URL: http://localhost:{PORT}")
            print(f"  Local File: {os.path.join(DIRECTORY, 'index.html')}")
            print("=======================================================================")
            print("  Opening browser automatically... Press Ctrl+C to stop.")
            threading.Thread(target=open_browser, daemon=True).start()
            httpd.serve_forever()
    except OSError as e:
        print(f"Port {PORT} is busy or restricted ({e}). Trying port 8081...")
        try:
            with socketserver.TCPServer(("", 8081), Handler) as httpd:
                print(f"  Web URL: http://localhost:8081")
                threading.Thread(target=lambda: webbrowser.open("http://localhost:8081"), daemon=True).start()
                httpd.serve_forever()
        except Exception:
            print(f"Opening index.html directly in browser...")
            webbrowser.open(os.path.join(DIRECTORY, 'index.html'))
