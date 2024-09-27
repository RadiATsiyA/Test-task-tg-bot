from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_API = os.getenv('TG_BOT_API')
CURRENCY_API_URL = os.getenv('CURRENCY_API_URL')