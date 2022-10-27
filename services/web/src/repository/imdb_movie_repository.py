import os

import requests

class IMDBMovieRepository():
    def get(self, imdb_movie_id):
        imdb_key = os.getenv("IMDB_KEY")
        url = f"http://www.omdbapi.com/?apikey={imdb_key}&i={imdb_movie_id}"
        response = requests.get(url)
        return response.json()


