# Melp Project
REST API built in Django with PostGis

## Why Django
Django is the most famous and supported python web framework, is focused on reducing the development time, is compatible with major operating systems and easy to extend and scale.

## Requirements
### For Dockerized app
- Docker >= 19.03
- Docker Compose >= 1.26

## Usage
For dockerized app the service will run in "127.0.0.1:8000"
### For Dockerized app
First run the cointainer for the db
```bash
docker-compose up --build -d db
```
After the db service is ready, then run the container for the web service 
```bash
docker-compose up --build -d web
```

(Optional) List all running Docker containers to verify the success of the building
```bash
docker ps
```

Then create the database migrations and populate with the initial data
```bash
docker-compose exec web python manage.py migrate
```

## Heroku Deployment
In the Heroku dashboard create an app and attach it the Heroku Postgres add-on, then by the Heroku CLI run the commands below:
### CLI Login
```bash
heroku login
```
### Postgres configuration
```bash
heroku pg:psql -a <app_name>
```
```bash
=> CREATE EXTENSION postgis;
=> SELECT postgis_version();
=> \q
```
### Docker
```bash
heroku container:login
heroku container:push web -a <app_name>
heroku container:release web -a <app_name>
```
### Migrate the data to Postgres
```bash
heroku run python manage.py makemigrations -a <app_name>
heroku run python manage.py migrate -a <app_name>
```

## API Documentantion
[a link](https://documenter.getpostman.com/view/12280244/T1LFoWF3)