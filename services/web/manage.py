from datetime import date, datetime
from werkzeug.security import generate_password_hash

from flask.cli import FlaskGroup
# from flasgger import Swagger

from src import db, create_app
from src.entity.movie import Movie
from src.entity.showtime import ShowTime
from src.entity.user import User

app = create_app()

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    new_movie = Movie(
        name="The Fast and the Furious",
        release_date=date(2001, 6, 22),
        imdb_rating=6.8,
        runtime="106 min"
    )
    db.session.add(new_movie)

    new_showtime = ShowTime(
        date=date(2022, 6, 10),
        time=datetime.now(),
        price=20.00,
        movie_id=1
    )
    db.session.add(new_showtime)

    new_cinema_owner = User(
        username="cinemaowner1",
        password=generate_password_hash("abc123"),
        role="cinemaowner"
    )
    db.session.add(new_cinema_owner)

    new_cinema_owner = User(
        username="moviegoer1",
        password=generate_password_hash("abc123"),
        role="moviegoer"
    )
    db.session.add(new_cinema_owner)

    db.session.commit()


if __name__ == "__main__":
    cli()
