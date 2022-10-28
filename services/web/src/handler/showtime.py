import datetime

from flask_restful import Resource, abort, reqparse
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_apispec import marshal_with
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields

from src.presenter.showtime import ShowTimeSchema, ShowTimeView
from src.usecase.user.service import UserService
from src.repository.user_repository import UserRepository

auth = HTTPBasicAuth()

# user
user_rep = UserRepository()
user_service = UserService(user_rep)

@auth.verify_password
def verify_password(username, password):
    user = user_service.find_by_username(username)
    if user is not None and user.role == 'cinemaowner' and check_password_hash(user.password, password):
        return user.username

class ShowTimeHandler(Resource):
    method_decorators = {'post': [auth.login_required]}

    parser = reqparse.RequestParser()
    parser.add_argument(
            'date',
            type=str,
            required=True,
            help='Date is required'
        )
    parser.add_argument(
            'price',
            type=float,
            required=True,
            help='Price is required'
        )
    parser.add_argument(
            'times',
            action='append'
        )

    def __init__(self, **kwargs):
        self.service = kwargs.get('service')

    def get(self, movie_id):
        """
        Get the Show Times of a Movie
        ---
        tags:
          - ShowTime
        parameters:
          - in: path
            name: movie_id
            type: integer
        responses:
          200:
            description: Show times of the movie
        """
        showtime_json = {"movie": movie_id, "show_times": []}
        showtimes = self.service.find_all_by_movie(movie_id)
        try:
            showtimes = self.service.find_all_by_movie(movie_id)
            for showtime in showtimes:
                showtime_view = ShowTimeView(
                        showtime.id,
                        showtime.date,
                        showtime.time,
                        showtime.price
                        )

                showtime_json.get("show_times").append(showtime_view.json())
        except Exception:
            pass

        return showtime_json

    def post(self, movie_id):
        """
        Create a new schedule and pricing for a movie
        ---
        tags:
          - ShowTime
        parameters:
          - in: path
            name: movie_id
            type: integer
          - in: body
            name: value
            description: JSON parameters
            schema:
              properties:
                date:
                  type: string
                  description: The date of the showing 
                  example: "2001-05-22"
                times:
                  type: array
                  description: The list of times available in HH:MM
                  example: ["07:41", "08:31"]
                price:
                  type: float
                  description: The price of a ticket
                  example: 20.50
        responses:
          200:
            description: OK
        """
        args = ShowTimeHandler.parser.parse_args()
        raw_date = args.date
        show_date = datetime.datetime.strptime(raw_date, '%Y-%m-%d')

        try:
            self.service.delete_by_movie(movie_id)

            for time in args['times']:
                movie_time = datetime.datetime.strptime(time, '%H:%M').time()
                self.service.create(
                    date=show_date,
                    time=movie_time,
                    price=args.price,
                    movie_id=movie_id
                )

        except Exception:
            abort(400, message="An error occurred.")

        return "OK", 201
