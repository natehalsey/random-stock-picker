FROM python:3.10-slim

RUN apt-get update && apt-get -y install cron

WORKDIR /var/task

COPY .env ./
COPY src ./
COPY requirements.txt ./

RUN pip install pip-tools
RUN pip-sync requirements.txt

COPY configs/daily-stock-cron /etc/cron.d/daily-stock-cron

RUN chmod 0644 /etc/cron.d/daily-stock-cron

RUN crontab /etc/cron.d/daily-stock-cron

RUN touch /var/task/cron.log

CMD ["/bin/bash", "-c", "cron && tail -f /var/task/cron.log"]
