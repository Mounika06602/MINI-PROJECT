from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()



"""
mongo conection
db
collections - users, notes
MONGODB_URI= mongodb+srv://Mounika:mouni123@cluster0.82umbdb.mongodb.net/?appName=Cluster0
DB_NAME= Notes_DB
USERS = NOTES_USERS
NOTES= SMART_NOTES

"""

uri = os.getenv("MONGODB_URI")

db = os.getenv("DB_NAME")
user = os.getenv("USERS")
notes = os.getenv("NOTES")

connection = MongoClient(uri)

database = connection[db]
notes_coll = database[notes]
