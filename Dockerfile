FROM python:3.7-slim
LABEL maintainer="oleg.gr@outlook.com"

RUN apt-get update && \
    apt-get install -y curl cron && \
    apt-get clean

WORKDIR /usr/src/app
COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r Requirements.txt
RUN chmod +x /usr/src/app/Scripts/dockerstart.sh

EXPOSE 80
CMD ["/usr/src/app/Scripts/dockerstart.sh"]