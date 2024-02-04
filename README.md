# random-stock-picker

Random stock picker is a cron job that pulls data from `ftp.nasdaqtrader.com` and then publishes an SMS using twilio to a phone. Inspired by: https://github.com/RayBB/random-stock-picker and adapted to be used with twilio.

# Getting started

First ensure `docker, docker-compose` and all dependencies are installed.

```
git clone https://github.com/natehalsey/random-stock-picker
```

Then you'll need to get your twilio information from twilio and set it in a `.env` file in the root of the project.

```
# .env

TWILIO_ACCOUNT_SID=""
TWILIO_AUTH_TOKEN=""
TWILIO_NUMBER=""
TO_NUMBER=""
```

Afterward, simply run:

```
. script/start-docker
```
And the cron job will be running inside of a docker container. 

# Customization

Currently the cron job will execute everday at 8:30 am EST. Edit the file in `configs/daily-stock-cron` to match to your specific needs.

# Local Dev

Install:

```
- pyenv
- virtualenv
```

Then simply `. .script/bootstrap` to bootstrap the environment and begin developing.
