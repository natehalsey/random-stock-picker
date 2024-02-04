import logging
import os

from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/task/cron.log'),
    ]
)


class Config:
    TWILIO_ACCOUNT_SID="fake-account-sid"
    TWILIO_AUTH_TOKEN="fake-auth-token"
    TWILIO_NUMBER="fake-number"
    TO_NUMBER="fake-number"

    @classmethod
    def load_from_env(cls):
        for key, value in vars(cls).items():
            if key.isupper() and not key.startswith("__"):
                setattr(cls, key, os.getenv(key, value))

load_dotenv()
Config.load_from_env()
