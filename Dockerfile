FROM python:3.8.10
WORKDIR /app
COPY . .
ENV MY_VAR=helloWorld
RUN pip3 install -r requirements.txt
EXPOSE 5001
ENTRYPOINT python3 -m pytest