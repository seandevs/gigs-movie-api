from datetime import date

from flask.cli import FlaskGroup

from src import db, create_app
from src.entity.movie import Movie

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
    db.session.commit()


if __name__ == "__main__":
    cli()
