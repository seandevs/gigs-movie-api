from src import db


class ShowTime(db.Model):
    __tablename__ = 'showtimes'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    price = db.Column(db.Float)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
