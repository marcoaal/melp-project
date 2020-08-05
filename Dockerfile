FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN apt-get update -qq && apt-get install -y -qq \    
    #geodjango
    gdal-bin binutils libproj-dev libgdal-dev

RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

CMD gunicorn melp_project.wsgi:application --bind 0.0.0.0:$PORT