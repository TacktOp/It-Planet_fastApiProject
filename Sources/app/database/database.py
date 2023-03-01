import pymongo.database
from pymongo import MongoClient
from pydantic import EmailStr
from bson.objectid import ObjectId
from fastapi import HTTPException

from ..models.models import Profile, Locations

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

        if self.profile.find_one({'_id': ObjectId(accountId)}) is None:
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

        if self.profile.find_one({'_id': ObjectId(accountId)}) is None:
            return HTTPException(status_code=403)
        else:
            self.profile.delete_one({'_id': ObjectId(accountId)})
            return HTTPException(status_code=200)


    def location_get(self, pointId: str):
        if pointId is None:
            return HTTPException(status_code=400)

        data = self.locations.find_one({'_id': ObjectId(pointId)})
        if data is None:
            return HTTPException(status_code=404)
        else:
            data['id'] = data['_id']
            return Locations(**data)

    def location_post(self, latitude: float, longitude: float):
        if self.locations.find_one({'latitude': latitude, 'longitude': longitude}) is not None:
            return HTTPException(status_code=409)

        if latitude is None or latitude < -90 or latitude > 90 or \
            longitude is None or longitude < -180 or longitude > 180:
            return HTTPException(status_code=400)
        else:
            data = Locations(
                latitude=latitude,
                longitude=longitude
            )
            self.locations.insert_one(data.dict())
            return HTTPException(status_code=201)

    def location_put(self, pointId: str, latitude: float ,longitude: float):
        if pointId is None or \
            latitude is None or latitude < -90 or latitude > 90 or \
            longitude is None or longitude < -180 or longitude > 180:
            return HTTPException(status_code=400)

        if self.locations.find_one({'_id': ObjectId(pointId)}) is None:
            return HTTPException(status_code=404)

        if self.locations.find_one({'latitude': latitude, 'longitude': longitude}) is not None:
            return HTTPException(status_code=409)
        else:
            self.locations.update_one({'_id': ObjectId(pointId)}, {'$set': {'latitude': latitude,
                                                                            'longitude': longitude
                                                                            }
                                                                   }
                                      )

            return HTTPException(status_code=200)

    def location_delete(self, pointId):
        if pointId is None:
            return HTTPException(status_code=400)

        if self.locations.find_one({'_id': ObjectId(pointId)}) is None:
            return HTTPException(status_code=404)
        else:
            self.locations.delete_one({'_id': ObjectId(pointId)})
            return HTTPException(status_code=200)