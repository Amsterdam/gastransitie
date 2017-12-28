FROM amsterdam/docker_python:latest
MAINTAINER datapunt@amsterdam.nl

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

RUN apt update \
	&& apt -y upgrade \
	&& apt -y install \
			gdal-bin \
			libgeos-dev \
			netcat \
	&& apt clean \
	&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
	&& adduser --system datapunt \
	&& mkdir -p /static \
	&& chown datapunt /static \
	&& pip install uwsgi

WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

USER datapunt
COPY ./app/ /app/
COPY ./deploy/ /deploy/

#COPY ./deploy/import /.jenkins-import/
#
#RUN python manage.py collectstatic --noinput
#
## Production no waits / migrates etc.
#CMD ["/deploy/docker-run.sh"]