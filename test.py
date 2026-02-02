"""from pymongo import MongoClient
from datetime import datetime
import sys

import os

uri = os.getenv("MONGODB_URI")

db = os.getenv("DB_NAME")
user = os.getenv("USERS")
notes = os.getenv("NOTES")

connection = MongoClient(uri)
database= connection["db"]
collections= database["user"]
collections.insert_one({
    "name": "Mouni",
    "email": "mouni@123.com",
    "password": "1234566555",
    "status": "active"
})
print(collections)
"""








from pymongo import MongoClient
from datetime import datetime
import os
uri = os.getenv("MongoDB_URL")
db = os.getenv("DB_NAME")
user = os.getenv("Users")
notes = os.getenv("NOTES")

connection = MongoClient(uri)
database= connection["db"]
collections= database["user"]
collections.insert_one({
    "name": "Mouni",
    "email": "mouni@123.com",
    "password": "1234566555",
    "status": "active"
})






