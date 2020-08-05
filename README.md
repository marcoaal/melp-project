# Melp Project
REST API built in Django with PostGis

## Why Django and PostGis
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