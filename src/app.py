from flask import Flask
from src.hello.routes import hello_routes

def create_app():
    app = Flask(__name__)
    app.register_blueprint(hello_routes)
    return app
