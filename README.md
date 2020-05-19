[![Build Status](https://travis-ci.org/BuildForSDG/team-195.svg?branch=develop)](https://travis-ci.org/BuildForSDG/team-195)

- [Part1](#part1)
    1. [Getting Started](#getting-started)
    1. [Project Structure](#project-structure)
    1. [Docker Config](#docker-config)
    1. [Postgres Setup](#postgres-setup)
    1. [Test Setup](#test-setup)
    1. [Django Tutor backend](#django-blueprints)
    1. [Graphql vs RESTful Routes](#graphql-vs-restful-routes)
    1. [Deployment](#deployment)
    2. [Workflow](#workflow)
    3. [Structure](#structure1)
- [Part2](#part2)
    1. [Introduction](#introduction)
    1. [Code Coverage and Quality](#code-coverage-and-quality)
    1. [Continuous Integration](#continuous-integration)
    2. [React Setup](#react-setup)
    3. [Testing React](#testing-react)
    4. [React Components](#react-components)
    5. [React Authentication](#react-authentication)
    6. [React and Docker](#react-and-docker)
    7. [Mocking react components](#mocking-react-components)

- [Part3](#part3)
    1. [Introduction](#part3-introduction)
    1. [Django Migrations](#django-migrate)
    1. [Django Bcrypt/JWT Authentication ](#django-authentication)
    1. [JWT Setup](#jwt-setup)
    1. [Auth Routes](#auth-routes)
    1. [React Router](#react-router)
    1. [React testing](#react-testing)
    1. [React Authentication - part 1](#react-authentication---part-1)
    1. [Mocking User Interaction](#mocking-user-interaction)
    1. [React Authentication - part 2](#react-authentication---part-2)
    1. [Authorization](#authorization)
    1. [Update Component](#update-component)
    1. [Update Docker](#update-docker)
    1. [Structure](#structure3)
    1. [End-to-End Test Setup](#end-to-end-test-setup)

**[Tutor](https://github.com/BuildForSDG/team-195)

Team 195 SDG Goal 4: Quality Education Implantation

This is as an Online learning platform application to manage courses, students, tutors, with a goal of increasing the number of qualified teachers in a community by providing online remote learning resources and platform to link tutors.

## <a name="part1"></a>Part1

### <a name="getting-started"></a>Getting Started

```bash
$ mkdir team-195 && cd team-195
$ cookiecutter https://github.com/pydanny/cookiecutter-django.git

$ cd tutor
$ pipenv --three && pipenv shell
$ pipenv install -r requirements/base
$ python manage.py migrate
$ python manage.py createsuperuser
```

### <a name="project-structure"></a>Project Structure

The bootstrapped Django app has the following:

“config” includes all the settings for our local and production environments.
“requirements” contains all the requirement files - base.txt, local.txt, production.txt - which you can make changes to and then install via `pipenv install -r file_name` .
“django_cookiecutter_docker” is the main project directory which consists of the “static”, “contrib” and “templates” directories along with the users app containing the models and boilerplate code associated with user authentication.
The environment files for each service in the .envs directory and add the required variables.

### <a name="docker-config"></a>Docker Config
The docker yaml template we will be editing is. To use docker make sure that docker service is installed on your PC, linux or MaC.
You can get the [docker Compose Docker Machine](https://docs.docker.com/)
