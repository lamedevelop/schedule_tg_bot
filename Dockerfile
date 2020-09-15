FROM python:3.7.2-alpine3.8
LABEL maintainer="oleg.gr@outlook.com"

WORKDIR /Users/my_app
COPY . .

RUN pip install --upgrade pip
#COPY Requirements.txt .
RUN pip install --no-cache-dir -r Requirements.txt
#COPY . ./app

ENTRYPOINT [ "python", "./Bot.py" ]
EXPOSE 80