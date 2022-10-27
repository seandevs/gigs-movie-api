# Gigs Movie API

## Development
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
$ curl --request POST --url http://localhost:5000/v1/movies/schedule/{movie_id} --header 'Content-Type: application/json' --data '{"date":"2001-06-22", "times": ["07:41"], "price": 20.20}'
```

## Running Tests
Within the `service/web` directory.
```
$ python -m unittest
```
