# TECHS Draft

Boilerplate project


## Contributing Guide

[CONTRIBUTING.md](CONTRIBUTING.md)


## Things to do after cloning this repository

1. Update `setup.py` contents with project details
2. Update `docker-compose.yml` and `docker-compose.local.yml` with project details
3. Update `.github/workflows/main.yml` with project details


## Development Setup

There are two ways to run for development: with Docker or with manual/traditional setup


### Backend Manual Setup

This method will make the development server run on your machine, and is advantageous when you want to do some quick changes and see the changes as you update the code.

**Requirements**
- Python == `3.9`

``` bash
# Environment setup
$ cd ./src
$ pip install pipenv
$ pipenv install -d --three
$ pipenv run pre-commit install

$ pipenv run uvicorn app.main:app --reload
```

### Using setup.py with Pipenv

```bash
$ cd ./src
$ pipenv install -e .
```

or

```bash
$ cd ./src
$ pipenv shell
$ pip install -e .
```

### Run App in Docker Compose

```bash
$ docker-compose -f docker-compose.local.yaml up
```

### Docs URL

http://localhost:8000/techs-draft/docs

### DB Migrations

To create a migration.

``` bash
$ pipenv run alembic revision --autogenerate -m "your comment"
```

### DB Forward Migration
You can upgrade one or more revision
``` bash
$ pipenv run alembic upgrade #num % e.g +1
```
or upgrade to the latest migration.
``` bash
$ pipenv run alembic upgrade head
```
