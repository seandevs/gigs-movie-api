from unittest import TestCase, mock

from src.repository.movie_repository import MovieRepository
from src.usecase.movie.service import MovieService
from src.entity.movie import Movie


def mock_movie():
    return Movie(
        name="The fast and the Furious"
    )

class TestMovieService(TestCase):
    def test_movie_not_existant(self):
        """Movie should not exist and should return None"""
        non_existant_movie_id = 1
        with mock.patch("src.repository.movie_repository.MovieRepository.get", return_value=None):
            self.assertIsNone(MovieService(MovieRepository()).get(non_existant_movie_id))

    def test_movie_existant(self):
        """Movie should exist and should match on movie name"""
        mocked_movie = mock_movie()
        movie_id = 1
        with mock.patch("src.repository.movie_repository.MovieRepository.get", return_value=mock_movie()):
            self.assertEqual(MovieService(
                MovieRepository()).get(movie_id).name,
                mocked_movie.name
                )
        

