from src.entity.movie import Movie


class MovieRepository():
    def get(self, id_):
        return Movie.query.get(id_)
