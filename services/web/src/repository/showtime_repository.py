from src import db
from src.entity.showtime import ShowTime


class ShowTimeRepository():
    def get(self, id_):
        return ShowTime.query.get(id_)

    def create(self, data):
        try:
            db.session.add(data)
            db.session.commit()
        except Exception:
            db.session.rollback()
        finally:
            db.session.close()

    def delete(self, id_):
        try:
            showtime = self.get(id)
            db.session.delete(showtime)
            db.session.commit()
        except Exception:
            db.session.rollback()
        finally:
            db.session.close()

    def delete_by_movie(self, movie_id):
        try:
            showtimes = ShowTime.query.filter_by(movie_id=movie_id).all()
            for showtime in showtimes:
                db.session.delete(showtime)
            db.session.commit()
        except Exception:
            db.session.rollback()
        finally:
            db.session.close()
