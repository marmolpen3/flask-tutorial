from flask import Flask, g
from middleware import hello_middleware
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask('app')

SWAGGER_URL = '/api/docs'  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API url (can of course be a local resource)

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Test application"
    },
)

app.register_blueprint(swaggerui_blueprint)

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