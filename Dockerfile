FROM python:3.7-alpine3.11

RUN apk add gcc postgresql-dev musl-dev curl postgresql --no-cache --quiet

WORKDIR /usr/src/app

COPY . .

RUN pip install -q --upgrade pip
RUN pip install --no-cache-dir -r Requirements.txt
RUN chmod +x /usr/src/app/Scripts/dockerstart.sh

EXPOSE 80
