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

## Calling Endpoints
### Movie
```
# GET a movie by ID
$ curl --request GET \
  --url http://localhost:5000/v1/movies/{movie_id}
```

###ShowTimes
```
# POST showtimes by movie ID
$ curl --request POST --url http://localhost:5000/v1/movies/{movie_id}/schedule --header 'Content-Type: application/json' --data '{"date":"2001-06-22", "times": ["07:41"], "price": 20.20}'
```

```
$ GET showtimes by movie ID
$ curl --request GET \
  --url http://localhost:5000/v1/movies/{movie_id}/schedule
```

####IMDB Movie
```
# GET an IMDB movie by ID (make sure to update your API key in env.dev)
$ curl --request GET \
  --url http://localhost:5000/v1/imdb_movies/{imdb_movie_id}
```

## Running Tests
Within the `service/web` directory.
```
$ python -m unittest
```
