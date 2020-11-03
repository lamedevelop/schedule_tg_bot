FROM python:3.7-slim-buster
LABEL maintainer="oleg.gr@outlook.com"

WORKDIR /Users/my_app
COPY . .

RUN apt-get update
RUN apt-get install -y curl

#RUN yum install -y curl
CMD /bin/bash

RUN pip install --upgrade pip
#COPY Requirements.txt .
RUN pip install --no-cache-dir -r Requirements.txt
#COPY . ./app

ENTRYPOINT [ "python", "./Bot.py" ]
EXPOSE 80