from src import db
from src.entity.rating import Rating


class RatingRepository():
    def create(self, data):
        try:
            db.session.add(data)
            db.session.commit()
        except Exception as e:
            raise e
            db.session.rollback()
        finally:
            db.session.close()
