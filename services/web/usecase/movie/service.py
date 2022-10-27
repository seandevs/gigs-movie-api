from src.entity.movie import Movie


class MovieService():
    def __init__(self, repository):
        self.repository = repository

    def get(self, id_):
        return self.repository.get(id_)

