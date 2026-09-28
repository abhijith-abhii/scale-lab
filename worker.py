from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
import hashlib,time,json
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  if self.path=='/work':
   end=time.perf_counter()+.04
   while time.perf_counter()<end:hashlib.pbkdf2_hmac('sha256',b'load',b'salt',1000)
  body=json.dumps({'status':'ok'}).encode();self.send_response(200);self.send_header('Content-Type','application/json');self.end_headers();self.wfile.write(body)
 def log_message(self,*args):pass
if __name__=='__main__':ThreadingHTTPServer(('0.0.0.0',8080),Handler).serve_forever()
