from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object("src.config.Config")

    from .api import api_bp
    app.register_blueprint(api_bp)
    Swagger(app)

    db.init_app(app)

    return app
