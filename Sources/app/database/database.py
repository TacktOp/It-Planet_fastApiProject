import pymongo.database
from pymongo import MongoClient
from pydantic import EmailStr
from bson.objectid import ObjectId
from fastapi import HTTPException

from ..models.models import Profile

class Database:
    client: MongoClient
    db: pymongo.database.Database
    profile: pymongo.collection.Collection
    animals: pymongo.collection.Collection
    locations: pymongo.collection.Collection

    def __init__(self):
        self.client = MongoClient('mongodb://localhost:27017')
        self.db = self.client['it-planeta']
        self.profile = self.db['profile']
        self.animals = self.db['animals']
        self.locations = self.db['locations']

    def account_get(self, accountId: str):
        if accountId is None:
            return HTTPException(status_code=400)

        data = self.profile.find_one({'_id': ObjectId(accountId)})
        if data is None:
            return HTTPException(status_code=404)
        else:
            data['id'] = data['_id']
            return Profile(**data)

    def account_search_get(self, firstName: str = None,
                           lastName: str = None,
                           email: EmailStr = None,
                           fromm: int = 0,
                           size: int = 10
                           ):
        datas = self.profile.find({'firstName': firstName.lower(),
                                   'lastName': lastName.lower(),
                                   'email': email.lower()
                                   })

        sp = []
        for data in datas:
            data['id'] = data['_id']
            sp.append(Profile(**data))

        return sp

    def account_put(self, accountId: str,
                    firstName: str,
                    lastName: str,
                    email: EmailStr,
                    password: str
                    ):
        if accountId is None \
                or firstName is None \
                or lastName is None \
                or email is None \
                or password is None:
            return HTTPException(status_code=400)

        data = self.profile.find_one({'_id': ObjectId(accountId)})
        if data is None:
            return HTTPException(status_code=403)
        else:
            self.profile.update_one({'_id': ObjectId(accountId)}, {'$set': {'firstName': firstName.lower(),
                                                                            'lastName': lastName.lower(),
                                                                            'email': email.lower(),
                                                                            'password': password
                                                                            }
                                                                   }
                                    )
            return HTTPException(status_code=200)



    def account_delete(self, accountId: str):
        if accountId is None:
            return HTTPException(status_code=400)

        data = self.profile.find_one({'_id': ObjectId(accountId)})
        if data is None:
            return HTTPException(status_code=403)
        else:
            self.profile.delete_one({'_id': ObjectId(accountId)})
            return HTTPException(status_code=200)