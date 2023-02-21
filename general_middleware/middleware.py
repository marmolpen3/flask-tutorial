from werkzeug.wrappers import Request, Response

class Middleware():
    def __init__(self, app):
        self.app = app
        self.username = "admin"
        self.password = "admin"

    def __call__(self, environ, start_response):
        request = Request(environ)
        username = request.authorization['username']
        password = request.authorization['password']

        if username == self.username and password == self.password:
            environ['user'] = {
                "name": username
            }
            return self.app(environ, start_response)
        
        response = Response("Unauthorized", 401, mimetype='text/plain')
        return response(environ, start_response)