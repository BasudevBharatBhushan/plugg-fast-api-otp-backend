from pymongo import MongoClient
from utils.logging import logging

try:
    client = MongoClient(host='mongodb+srv://admin-basudev:OoAkYrt6dz3DGZQF@cluster0.nbsww.mongodb.net/?retryWrites=true&w=majority')
    db = client.pluggwaitlist
    collection = db.users
    logging.info("Connected to database")
except Exception as e:
    logging.error("Failed to connect to database: %s", str(e))
    raise Exception("Failed to connect to database")