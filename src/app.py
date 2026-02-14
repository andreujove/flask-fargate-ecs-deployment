from flask import Flask
import os
from src.hello.routes import hello_routes

def create_app():
    app = Flask(__name__)
    os.makedirs(app.instance_path, exist_ok=True)
    app.register_blueprint(hello_routes)
    return app
