from src import db


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    release_date = db.Column(db.Date)
    imdb_rating = db.Column(db.Float)
    runtime = db.Column(db.String(50))
    showtimes = db.relationship('ShowTime', backref='movie')
    ratings = db.relationship('Rating', backref='movie')
