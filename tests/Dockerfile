# Derived from official mysql image (our base image)
# Use mysql 5.7 as the flask-app is not set up to work with later versions
FROM mysql:5.7

# Add a database and root password
# For hints on how to do this, consult the mysql 5.7 image documentation
ENV MYSQL_DATABASE test
FROM python:3.8.10
WORKDIR /app
COPY ./tests/test.sql /docker-entrypoint-initdb.d/
ENV DB_PASSWORD=${DB_PASSWORD}
RUN pip3 install -r requirements.txt

