from flask import Flask, Blueprint
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("src.config.Config")

    from .api import api_bp
    app.register_blueprint(api_bp)

    db.init_app(app)

    return app
