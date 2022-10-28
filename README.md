# Gigs Movie API
This is an API for interacting with a Movie API based on the requirements located at <https://gist.github.com/wbaumann/aaa5ef095e213ffbea35b7ca3cc251a7>.

## Design Decisions
#### Language and Framework
Python and Flask were chosen because this is the current language and framework of Gigs.

#### Architecture
The architecture of the application is based off the **Clean Architecture**. This makes it easier to write tests in isolation due to dependency injection as well as swap out data access without re-writing the business logic. An example of this can be found when comparing the **movie** entity that hits the postgres instance versus the **IMDB movie** which hits a third party API.  

The **handler** accepts a request and then calls the **usecase service** which calls the **entity** if creating a new object but ultimately calls the **repository** which calls the **db** eventually bubbling results back to the **handler** which presents the results (where appropriate) using the **presenter**.  

#### Authentication / Authorization
For simplicity a Basic Auth scheme was implemented for authentication and authorization however typically this would be replaced with a more sophisticated token model. Basic Auth was chosen simply for illustrative purposes. Flask has a number of libraries for implementing a more hardened model.  

#### Containerization
The app is dockerized for simplicity of development.  

#### Development model
Because this did not require 100% test coverage, the app was developed code first and then tests. The tests are there just to show the various forms as requested. In a real-world production environment TDD would have been done with a much higher code coverage.

## Development
Update the `IMDB_KEY` in `.env.dev` with your API Key.  

Note that when you seed the database, there are 2 usertypes:
- cinema owner: `username: cinemaowner1, password: abc123`  
- movie goer: `username: moviegoer1, password: abc123`  

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

### Swagger Docs
Swagger docs can be found at `localhost:5000/apidocs`.
