FROM python:3.7-slim-buster
LABEL maintainer="oleg.gr@outlook.com"


RUN apt-get update && \
    apt-get install -y curl cron && \
    apt-get clean

RUN apt-get install sqlite3
#RUN yum install -y curl

WORKDIR /Users/my_app
COPY . .

RUN pip install --upgrade pip
#COPY Requirements.txt .
RUN pip install --no-cache-dir -r Requirements.txt
#COPY . ./app

#ENTRYPOINT [ "python", "./Bot.py" ]



EXPOSE 80
CMD ["/Users/my_app/Scripts/dockerstart.sh"]