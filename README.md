# Flask Rest API Setup

Initial scaffolding for a flask rest API development. Starter template for building your Flask and Flask Rest API applications.

## Features
- Gunicorn server setup
- Database migration setup for SQLAlchemy Models
- JWT authentication at `<your-host>/api/v1/login`
- Url to register your admin and users at `<your-host>/api/v1/signup`
- Provisioned route file for all your routes with admin blueprints
- Test environment setup

## Built With

This App was developed with the following stack:

- Python==3.12
- Flask==3.10
- Flask-restful==0.3.10
- Flask-Script==2.0.6
- Flask-SQLAlchemy==3.1.1
- Postgres DB / SQlite
- Gunicorn Web Server

## Requirements
- Python 3.12+
- Python pip
- Postgres / SQlite

## Installation
- fork this repository
- create a .env file as shown in the env_example file
- setup your database 
- on the terminal cd into the app folder 
- run `pip install -r requirements.txt` to install required modules
- run `flask --app manage db init ` to setup alembic migrations
- run `flask --app manage db migrate -m='<your migration message>'` to create migration files
- then run `flask --app python manage db upgrade` to create tables

## Running the App
- on the terminal run `gunicorn main:app`
- To run app on a specific port use `gunicorn -127.0.0.1:port main:app`

## Usage
- `src/api/resources` --- flask-restful resources for your project
- `src/models` --- SQLAlchemy models and schema
- `src/routes/api` --- contains all your route definition
- `src/utils` --- contains validations, security and helper files
- `src/middlewares` --- define your middleware files here
- You can modify the app to suit your need.
- Happy usage.

## Update Information
- Flask-JWT has been replaced with Flask-JWT-extended
- Flask-Scripts and dependencies removed.
- Future versions may use Pydantic instead of Marshmallow

## Contributions
- Contributors are needed to keep developing this template with updates to its dependencies. You can reach me on my email.

## Credits
solnsumei@gmail.com
