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
# GET
$ curl --request GET \
  --url http://localhost:5000/movies/{movie_id}
```

## Running Tests
Within the `service/web` directory.
```
$ python -m unittest
```
