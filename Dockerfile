FROM python:3-alpine

WORKDIR /usr/src/app

VOLUME /logs

COPY . .

CMD [ "python", "./monitor.py" ]