# pull official base image
FROM python:3.10-alpine
# add and run as non-root user
RUN adduser -D myuser

EXPOSE 8080
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# set work directory
WORKDIR /app
# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
#run the server
CMD gunicorn streetview.wsgi:application --bind 0.0.0.0:8080

