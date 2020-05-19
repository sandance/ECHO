This is a [Docker][] setup for a web application based on Django.

## Requirements
You need to install [Docker][] and [Docker-Compose][].

## Build
`docker-compose build` or `make build`.

## Migrate databases
`docker-compose run --rm djangoapp hello/manage.py migrate` or `make migrate`.

## Collect static files
`docker-compose run --rm djangoapp hello/manage.py collectstatic --no-input'` or `make collectstatic`.

## Run
`docker-compose up` or `make run`.

## Tests
- `make checksafety`
- `make checkstyle`
- `make test`
- `make coverage`

