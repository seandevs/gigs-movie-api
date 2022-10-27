from src.entity.showtime import ShowTime

class ShowTimeService():
    def __init__(self, repository):
        self.repository = repository

    def create(self, date, time, price, movie_id):
        showtime = ShowTime(
                date=date, 
                time=time, 
                price=price, 
                movie_id=movie_id
            )
        return self.repository.create(showtime)
