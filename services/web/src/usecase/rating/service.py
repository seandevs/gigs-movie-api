from src.entity.rating import Rating


class RatingService():
    def __init__(self, repository):
        self.repository = repository

    def create(self, value, user_id, movie_id):
        rating = Rating(
                value=value,
                user_id=user_id,
                movie_id=movie_id
            )
        return self.repository.create(rating)
