class MovieHandler(Resource):

    def __init__(self, **kwargs):
        self.service = kwargs['service']

    def get(self, movie_id):
        try:
            movie = self.service.get(movie_id)
        except Exception:
            abort(404, message=f"Movie with {movie_id} doesn't exist")

        movie_view = MovieView(
                movie_id,
                movie.get('name'),
                movie.get('release_date'),
                movie.get('imdb_rating'),
                movie.get('runtime')
            )

        return movie_view.json()

