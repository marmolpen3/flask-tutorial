from flask import Flask, request
from middleware import Middleware

app = Flask("app")
app.wsgi_app = Middleware(app.wsgi_app)

# This is a decorator that tells Flask what URL should trigger our function. 
@app.get("/")
def hello_world():
    user = request.environ['user']
    return f"Hello, {user}!"

if __name__ == "__main__":
    app.run()