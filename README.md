# Flask Rest API Setup

Initial scaffolding for a flask restful Api development. Starting point for your flask rest api projects.

## Features
- Gunicorn server setup
- Database migration setup for SQLAlchemy Models
- JWT authentication at `<your-host>/login`
- Url to register your admin and users at `<your-host>/api/v1/signup`
- All ready provisioned route file for all your routes with admin blueprints
- Test environment setup

## Built With

This App was developed with the following stack:

- Python
- Flask
- Flask-restful
- Postgres DB

## Requirements
- Python 3.6+
- Python pip
- Postgres SQL

## Installation
- fork this repository
- create a .env file as shown in the env_example file
- setup your database 
- on the terminal cd into the app folder 
- run `pip install -r requirements.txt` to install required modules
- run `python manage.py db migrate` to create migration files
- then run `python manage.py db upgrade` to create tables

## Running the App
- on the terminal run `gunicorn main:app`
- To run app on a specific port use `gunicorn -127.0.0.1:port main:app`

## Credits
solnsumei@gmail.com
