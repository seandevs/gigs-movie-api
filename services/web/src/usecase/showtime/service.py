from src.entity.showtime import ShowTime


class ShowTimeService():
    def __init__(self, repository):
        self.repository = repository

    def get(self, id_):
        return self.repository.get(id_)

    def find_all_by_movie(self, movie_id):
        return self.repository.find_all_by_movie(movie_id)

    def create(self, date, time, price, movie_id):
        showtime = ShowTime(
                date=date,
                time=time,
                price=price,
                movie_id=movie_id
            )
        return self.repository.create(showtime)

    def delete(self, id_):
        self.repository.delete(id_)

    def delete_by_movie(self, movie_id):
        self.repository.delete_by_movie(movie_id)
