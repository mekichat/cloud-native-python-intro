from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from users import add_user, list_users, user_exists, delete_user, update_user


class UserRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/users":
            users = list_users()
            
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            
            respponse_body = json.dumps(users)
            self.wfile.write(respponse_body.encode("utf-8"))
            
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode("utf-8"))
            
    def do_POST(self):
        if self.path =="/users":
           content_length = int(self.headers.get("Content-Length", 0))
           body = self.rfile.read(content_length)
           
           try:
               data =  json.loads(body.decode("utf-8"))
           except json.JSONDecodeError:
               self.send_response(400)
               self.end_headers()
               self.wfile.write(b"Invalid JSON")
               return
           
           if not isinstance(data, dict):
              self.send_response(400)
              self.end_headers()
              self.wfile.write(b"JSON must be an object")
              return
           

           name = data.get("name", "")
           age = data.get("age", "")
           success = add_user(name, age)

           if success:
               self.send_response(201)
               self.send_header("Content-type", "application/json")
               self.end_headers()
               self.wfile.write(json.dumps({"message": "User created"}).encode("utf-8"))
           else:
               self.send_response(400)
               self.send_header("Content-type", "application/json")
               self.end_headers()
               self.wfile.write(json.dumps({"error": "invalid or duplicate user"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not found"}).encode("utf-8"))
            
    
def run_server():
    server_address = ("", 8080)
    httpd = HTTPServer(server_address, UserRequestHandler)
    print("Server running on http://localhost:8080")
    httpd.serve_forever()
        
        
if __name__ == "__main__":
    run_server()