import datetime

from flask_restful import Resource, abort, reqparse

from src.presenter.showtime import ShowTimeView


class ShowTimeHandler(Resource):
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
        self.service = kwargs['service']

    def get(self, movie_id):
       showtimes = self.service.find_all_by_movie(movie_id) 
       showtime_json = {"movie": movie_id, "show_times": []}
       for showtime in showtimes:
           showtime_view = ShowTimeView(
                   showtime.id,
                   showtime.date,
                   showtime.time,
                   showtime.price
                )

           showtime_json.get("show_times").append(showtime_view.json())

       return showtime_json

    def post(self, movie_id):
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

        return "", 201
