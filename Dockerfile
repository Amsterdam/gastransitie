FROM amsterdam/docker_python:latest

ADD /entrypoint.sh /entrypoint.sh
RUN chmod u+x /entrypoint.sh

ENTRYPOINT /entrypoint.sh
