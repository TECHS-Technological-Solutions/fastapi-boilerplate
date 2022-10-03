# TECHS Draft

Boilerplate project


## Development Setup

There are two ways to run for development: with Docker or with manual/traditional setup


### Backend Manual Setup

This method will make the development server run on your machine, and is advantageous when you want to do some quick changes and see the changes as you update the code.

**Requirements**
- Python == `3.8`

``` bash
# Environment setup
$ cd ./src
$ pip install pipenv
$ pipenv install --three

$ pipenv run uvicorn app.main:app --reload
```

### Run App in Docker Compose

```bash
$ docker-compose -f docker-compose.local.yaml up
```

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
