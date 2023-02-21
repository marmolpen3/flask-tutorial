from flask import Flask, g
from middleware import hello_middleware

app = Flask('app')

# This is a decorator that tells Flask what URL should trigger our function. 
@app.get('/')
@hello_middleware
def hello_world():
    return f'Hello {g.user}!'

@app.get('/hello')
def hello_world_2():
    return 'Hello, World without middleware!'


if __name__ == "__main__":
    app.run()