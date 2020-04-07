import os
from databases import DatabaseURL

PROJECT_NAME = os.getenv("PROJECT_NAME", "jarvis")
DATABASE_URL = DatabaseURL(os.getenv("DATABASE_URL"))
MAX_CONNECTIONS_COUNT = int(os.getenv("MAX_CONNECTIONS_COUNT", 10))
MIN_CONNECTIONS_COUNT = int(os.getenv("MIN_CONNECTIONS_COUNT", 10))
WEBHOOK_SECRET_TOKEN = os.getenv("WEBHOOK_SECRET_TOKEN")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_ACCOUNT_AUTH_TOKEN = os.getenv("TWILIO_ACCOUNT_AUTH_TOKEN")
TWILIO_ACCOUNT_MESSAGING_SID = os.getenv("TWILIO_ACCOUNT_MESSAGING_SID")
TWILIO_PHONE_NUMBER_SID = os.getenv("TWILIO_PHONE_NUMBER_SID")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
TO_PHONE_NUMBER = os.getenv("TO_PHONE_NUMBER")
