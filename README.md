# Gigs Movie API

## Development
Update the `IMDB_KEY` in `.env.dev` with your API Key.  

Start the application with detached docker-compose.
```
$ docker-compose up -d
```

Create the database
```
$ docker-compose exec web python manage.py create_db
```

Seed the database
```
$ docker-compose exec web python manage.py seed_db
```

### Calling Endpoints
#### Movie
```
# GET a movie by ID

$ curl --request GET \
  --url http://localhost:5000/v1/movies/{movie_id}
```

#### ShowTimes
```
# POST showtimes by movie ID
# This is Basic Auth with the default user with username: cinemaowner1 and password: abc123

$ curl --location --request POST 'http://localhost:5000/v1/movies/1/schedule' \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Basic Y2luZW1hb3duZXIxOmFiYzEyMw==' \
  --data-raw '{"date":"2001-06-22", "times": ["07:41"], "price": 20.40}'
```

```
# GET showtimes by movie ID

$ curl --request GET \
  --url http://localhost:5000/v1/movies/{movie_id}/schedule
```

#### IMDB Movie
```
# GET an IMDB movie by ID (make sure to update your API key in env.dev)

$ curl --request GET \
  --url http://localhost:5000/v1/imdb_movies/{imdb_movie_id}
```

#### Rating
```
# Post ratings for Movie by ID
# This is Basic Auth with the default user with username: moviegoer1 and password: abc123

$ curl --location --request POST 'http://localhost:5000/v1/movies/1/rating' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic bW92aWVnb2VyMTphYmMxMjM=' \
--data-raw '{"value":10}'
```

### Running Tests
Within the `service/web` directory.
```
$ python -m unittest
```
