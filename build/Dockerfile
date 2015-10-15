#FROM python:2.7.10-wheezy
FROM debian:wheezy

RUN apt-get update && apt-get install -y wget python
RUN wget http://repo.ajenti.org/debian/key -O- | apt-key add -
RUN echo "deb http://repo.ajenti.org/debian main main debian" >> /etc/apt/sources.list
RUN rm /etc/apt/apt.conf.d/docker-gzip-indexes
RUN apt-get update && apt-get install -y ajenti

RUN sed -i "s@true@false@g" /etc/ajenti/config.json

EXPOSE 8000

VOLUME ["/etc/ajenti"]

ENTRYPOINT ["ajenti-panel"]
