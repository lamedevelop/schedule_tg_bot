FROM python:3.7-alpine3.11

RUN apk add \
    mariadb-dev \
    mariadb-client \
    gcc \
    musl-dev \
    curl \
    libc-dev \
    linux-headers \
    --no-cache --quiet

ARG PROJECT_PATH
WORKDIR $PROJECT_PATH

COPY . .

RUN pip install -q --upgrade pip
RUN pip install --no-cache-dir -r Requirements.txt
RUN chmod +x ${PROJECT_PATH}Scripts/dockerstart.sh

EXPOSE 80