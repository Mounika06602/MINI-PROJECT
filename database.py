from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


uri = os.getenv("MONGODB_URI")

db = os.getenv("DB_NAME")
user = os.getenv("USERS_COLLECTIONS")
notes = os.getenv("NOTES_COLLECTIONS")

connection = MongoClient(uri)

database = connection[db]
notes_coll = database[notes]
users_coll = database[user]