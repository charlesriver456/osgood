# Overview

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Downloads](https://static.pepy.tech/badge/osgood/month)](https://pepy.tech/project/osgood)

This is a small package of useful components.

## Docker

This package comes with a `Dockerfile` and `docker-compose` files to allow dockerized development if desired. Simply run `docker compose up -d` to run the containers in the `docker-compose.yml` in detached mode. See which containers are running by using `docker ps`. If you want to open a bash session inside one of the containers run `docker-compose exec <container-name> /bin/bash`. To stop all containers run `docker compose down`.

The build command in the `docker-compose.yml` takes care of building the `Dockerfile`. If you'd like to force a rebuild run `docker-compose up --build`.
