FROM mysql:5.7
FROM python:3.8.10
WORKDIR /app
COPY ./tests/test.sql /docker-entrypoint-initdb.d/
ENV DB_PASSWORD=${DB_PASSWORD}, MYSQL_DATABASE=test
RUN pip3 install -r
ENTRYPOINT pytest --cov