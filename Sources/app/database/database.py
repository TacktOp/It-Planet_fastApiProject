import pymongo.database
from pymongo import MongoClient
from bson.objectid import ObjectId

class Database:
    client: MongoClient
    db: pymongo.database.Database
    profile: pymongo.collection.Collection
    animals:pymongo.collection.Collection
    locations:pymongo.collection.Collection

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['default_db']
        self.profile = self.db['profile']
        self.animals = self.db['animals']
        self.locations = self.db['locations']