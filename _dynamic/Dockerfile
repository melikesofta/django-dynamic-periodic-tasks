# this Dockerfile defines the necessary elements to create the Docker image
# once the image is created, it can then be run as a Docker container

# set the base image
FROM python:3.9.0-buster

# create the project directory in the container
RUN mkdir /dynamic
WORKDIR /dynamic

# get the requirements file and install all the libraries
COPY ./requirements.txt /dynamic/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# copy and configure 'wait-for-it' script
COPY ./wait-for-it.sh /usr/local/bin/
RUN chmod u+x /usr/local/bin/wait-for-it.sh

# install postgresql client (for use with Django mgmt command dbshell)
RUN apt-get update
RUN apt-get install -y postgresql-client

# copy and configure custom entrypoint to wait for postgres then run webserver
COPY ./custom-entrypoint /usr/local/bin/
RUN chmod u+x /usr/local/bin/custom-entrypoint
ENTRYPOINT ["custom-entrypoint"]
