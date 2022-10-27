import datetime

from flask_restful import Resource, abort, reqparse


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


    def post(self, movie_id):
        args = ShowTimeHandler.parser.parse_args()
        raw_date = args.date
        show_date = datetime.datetime.strptime(raw_date, '%Y-%m-%d')

        try:
            for time in args['times']:
                movie_time = datetime.datetime.strptime(time, '%H:%M').time()
                showtime = self.service.create(
                    date=show_date,
                    time=movie_time,
                    price=args.price,
                    movie_id=movie_id
                )

        except Exception as e:
            abort(400, message="An error occurred.")

        return "", 201
