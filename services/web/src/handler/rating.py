import datetime

from flask_restful import Resource, abort, reqparse
from functools import wraps
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

from src.usecase.user.service import UserService
from src.repository.user_repository import UserRepository

auth = HTTPBasicAuth()

# user
user_rep = UserRepository()
user_service = UserService(user_rep)

@auth.verify_password
def verify_password(username, password):
    user = user_service.find_by_username(username)
    if user is not None and user.role == 'moviegoer' and check_password_hash(user.password, password):
        return user

class RatingHandler(Resource):
    method_decorators = {'post': [auth.login_required]}

    parser = reqparse.RequestParser()
    parser.add_argument(
            'value',
            type=int,
            required=True,
            choices=(1, 2, 3, 4, 5),
            help='The Rating value must be between 1 and 5'
        )

    def __init__(self, **kwargs):
        self.service = kwargs.get('service')

    def post(self, movie_id):
        """
        Post a rating for a movie.
        ---
        tags:
          - Rating
        parameters:
          - in: path
            name: movie_id
            type: integer
          - in: body
            name: value
            description: JSON parameters
            schema:
              properties:
                value:
                  type: integer
                  description: Rating value
                  example: 1
            
        responses:
          201:
            description: OK
        """
        args = RatingHandler.parser.parse_args()
        value = args.value
        try:
            self.service.create(
                    value=value,
                    user_id=auth.current_user().id,
                    movie_id=movie_id
                )
        except Exception:
            abort(400, message="An error occurred.")

        return "OK", 201
