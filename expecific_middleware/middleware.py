from functools import wraps
from flask import Response, request, g

def hello_middleware(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        username = request.authorization['username']
        password = request.authorization['password']
        if username == 'admin' and password == 'admin':
            g.user = username
            return func(*args, **kwargs)
        return Response('Could not verify your access.\n', 401, mimetype='text/plain')
       
    return decorated_function
