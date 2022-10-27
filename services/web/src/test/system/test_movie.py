import os
import unittest
import json
from datetime import date

from src import create_app, db
from src.entity.movie import Movie

fixture_data = (
    Movie(
        id=1,
        name="The Fast and the Furious",
        release_date=date(2001, 6, 22),
        imdb_rating=6.8,
        runtime="106 min"
    ),
)


class TestMovie(unittest.TestCase):
    def setUp(self):
        os.environ["DATABASE_URL"] = "sqlite://"
        app = create_app()
        app.testing = True
        self.app = app.test_client()
        self.app_context = app.app_context()
        self.app_context.push()

        db.reflect()
        db.drop_all()
        db.create_all()
        for movie in fixture_data:
            db.session.add(movie)

        db.session.commit()
        db.session.remove()

    def test_movie_not_existant(self):
        invalid_id = 0
        res = self.app.get(f"v1/movies/{invalid_id}")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(
                data.get("message"),
                f"Movie with id {invalid_id} doesn't exist"
            )

    def test_movie_existant(self):
        valid_id = 1
        res = self.app.get(f"v1/movies/{valid_id}")

        self.assertEqual(res.status_code, 200)
