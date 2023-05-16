from pymongo import MongoClient
import logging

DB_URL = 'mongodb+srv://admin-basudev:OoAkYrt6dz3DGZQF@cluster0.nbsww.mongodb.net/?retryWrites=true&w=majority'

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