from flask_restful import Resource, abort


class IMDBMovieHandler(Resource):

    def __init__(self, **kwargs):
        self.service = kwargs.get('service')

    def get(self, imdb_movie_id):
        """
        Get the IMDB Movie based on ID
        ---
        tags:
          - IMDB Movie
        parameters:
          - in: path
            name: imdb_movie_id
            type: string
            default: tt0232500
        responses:
          200:
            description: IMDB movie response
        """

        response = self.service.get(imdb_movie_id)

        if response.get("Response") == False:
            abort(404, message=f"IMDB Movie with id {imdb_movie_id} doesn't exist")

        return response
