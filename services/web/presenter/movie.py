from dataclasses import dataclass
from datetime import date


@dataclass
class MovieView:
    id_: int
    name: str
    release_date: date
    imdb_rating: float
    runtime: str

    def json(self):
        return {
                'id': self.id_,
                'name': self.name,
                'release_date': self.release_date,
                'imdb_rating': self.imdb_rating,
                'runtime': self.runtime
            }
