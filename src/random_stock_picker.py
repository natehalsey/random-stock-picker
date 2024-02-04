import logging
import random
import re

from ftplib import FTP
from twilio.rest import Client
from typing import List

from config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/task/cron.log'),
    ]
)

logger = logging.getLogger(__name__)


try:
    twilio_client = Client(
        Config.TWILIO_ACCOUNT_SID, 
        Config.TWILIO_AUTH_TOKEN,
    )

except Exception as e:
    logger.error("Failed to initialize twilio client: %s", str(e))
    raise

def get_nasdaq_data() -> List[str]:
    nasdaq_data = []
    
    try:
        ftp = FTP('ftp.nasdaqtrader.com')
        ftp.login()
        ftp.retrlines('RETR symboldirectory/nasdaqtraded.txt', nasdaq_data.append)
    except Exception as e:
        logger.error("FTP to nasdaqtrader.com failed: %s", str(e))
        raise
    
    return nasdaq_data

def get_random_stock():
    try:
        nasdaq_data: List[str] = get_nasdaq_data()
    except Exception as e:
        logger.error("Failed to get nasdaq data: %s", str(e))
        raise
    
    stock_symbols: List[str] = [re.search(r'^\w\|(\w*)', line).group(1) for line in nasdaq_data if re.match(r'^\w\|\w*', line)]
    
    return random.choice(stock_symbols)

def _create_text_body(stock_symbol: str):
    yahoo_link = f"https://finance.yahoo.com/quote/{stock_symbol}"
    return f"Stock of the day: {stock_symbol}, here's the yahoo finance link: {yahoo_link}"

def send_daily_stock_text() -> None:
    try:
        stock_symbol = get_random_stock()
    except Exception as e:
        logger.error("Failed to get random stock: %s", str(e))
        raise

    body = _create_text_body(stock_symbol)
    
    try:
        message = twilio_client.messages.create(
            to=Config.TO_NUMBER,
            from_=Config.TWILIO_NUMBER,
            body=body
        )
    except Exception as e:
        logger.error("Failed to send message: %s", str(e))
        raise

    logger.info(message)

if __name__ == "__main__":
    send_daily_stock_text()
