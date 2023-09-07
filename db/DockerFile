FROM python:3.8.10
WORKDIR /app
COPY . .
ENV MYSQL_DATABASE_PASSWORD=${DB_PASSWORD}
RUN pip3 install -r requirements.txt
EXPOSE 5001
ENTRYPOINT python3 app.py