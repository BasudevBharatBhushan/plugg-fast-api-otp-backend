from pymongo import MongoClient
from dotenv import load_dotenv, dotenv_values
from utils.logging import logging

load_dotenv()

db_config = dotenv_values(".env")
DB_URL = db_config.get("DB_URL")


if DB_URL is None:
    logging.error("DB_URL not found in environment variables")
    raise Exception("DB_URL not found")

try:
    client = MongoClient(host=DB_URL)
    db = client.pluggwaitlist
    collection = db.users
    logging.info("Connected to database")
except Exception as e:
    logging.error("Failed to connect to database: %s", str(e))
    raise Exception("Failed to connect to database")