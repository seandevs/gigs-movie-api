from flask_restful import Resource, abort
from flask_apispec import marshal_with
from flask_apispec.views import MethodResource

from src.presenter.movie import MovieSchema


class MovieHandler(MethodResource, Resource):

    def __init__(self, **kwargs):
        self.service = kwargs.get('service')

    @marshal_with(MovieSchema)
    def get(self, movie_id):
        """
        Get the Movie based on ID
        ---
        tags:
          - Movie
        parameters:
          - in: path
            name: movie_id
            type: integer
        responses:
          200:
            description: A movie response
            schema:
              properties:
                id:
                  type: integer
                  description: The id of the movie
                  default: 0
                imdb_rating:
                  type: float
                  description: The rating from IMDB
                  default: 0
                name:
                  type: string
                  description: The name of the movie
                release_date:
                  type: string
                  description: The release_date of the movie
                runtime:
                  type: string
                  description: The length of the movie
        """
        movie = self.service.get(movie_id)

        if not movie:
            abort(404, message=f"Movie with id {movie_id} doesn't exist")

        movie_schema = MovieSchema()

        return movie_schema.dump(movie)
        
