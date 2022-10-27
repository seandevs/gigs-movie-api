from src import db
from src.entity.showtime import ShowTime


class ShowTimeRepository():
    def create(self, data):
        committed = True
        try:
            db.session.add(data)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            committed = False
        finally:
            db.session.close()
        return committed
