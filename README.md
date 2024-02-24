# Overview

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![image](https://img.shields.io/pypi/v/osgood.svg)](https://pypi.org/project/osgood)
[![image](https://img.shields.io/pypi/l/osgood.svg)](https://pypi.org/project/osgood)
[![](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Downloads](https://static.pepy.tech/badge/osgood/month)](https://pepy.tech/project/osgood)

This is a small package of useful components.

## Docker

This package comes with a `Dockerfile` and `docker-compose` files to allow dockerized development if desired. Simply run `docker compose up -d` to run the containers in the `docker-compose.yml` in detached mode. See which containers are running by using `docker ps`. If you want to open a bash session inside one of the containers run `docker-compose exec <container-name> /bin/bash` (in this case `docker-compose exec osgood-app /bin/bash`). To stop all containers run `docker compose down`.

The build command in the `docker-compose.yml` takes care of building the `Dockerfile`. If you'd like to force a rebuild run `docker-compose up --build`.

To test:
Run `pytest` at the root of the repo.
