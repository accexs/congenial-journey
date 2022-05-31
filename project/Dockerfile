FROM python:3.10.1-slim-buster

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install pipenv and compilation dependencies
RUN apt-get update && apt-get install -y netcat gcc

# Install python dependencies in /.venv
RUN pip install --upgrade pip
RUN pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy
ENV PATH="/usr/src/app/.venv/bin:$PATH"

# add app
COPY . .
#CMD ["uvicorn", "app.main:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000"]