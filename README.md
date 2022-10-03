# TECHS Draft

Boilerplate project



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
