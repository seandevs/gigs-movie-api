from flask import Flask
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("src.config.Config")
db = SQLAlchemy(app)
api = Api(app)

class Test(db.Model):
    __tablename__ = "tests"
    id = db.Column(db.Integer, primary_key=True)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


api.add_resource(HelloWorld, '/')
