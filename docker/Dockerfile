FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

RUN pip3 install pipenv

# -- Adding Pipfiles
COPY ./src/Pipfile Pipfile
COPY ./src/Pipfile.lock Pipfile.lock

# -- Install dependencies:
RUN set -ex && pipenv install --system --dev --ignore-pipfile

COPY ./src /app

