class IMDBMovieService():
    def __init__(self, repository):
        self.repository = repository

    def get(self, id_):
        return self.repository.get(id_)

