import base64
from typing import List

import pymongo
from fastapi import APIRouter, HTTPException
from pydantic import EmailStr

from ..database.database import Database
from ..models.models import Profile

dbo = Database()
class User:
    """Роутер для Base аутентификации"""
    profileDB: pymongo.collection.Collection
    router = APIRouter()

    route_str = {
        "reg": "/registration",
        "login": "/login"
    }

    class Token:

        def encode(self, login: str, password: str) -> str:
            token = base64.b64encode(bytes(f'{login}:{password}', 'utf-8'))
            return "Basic " + token.decode("utf-8")

        def decode(self, token: str) -> List[str]:
            base64_str = token.split(" ")[1]
            return base64.b64decode(base64_str).decode("utf-8").split(":")

        def compare(self, login, password, token) -> bool:
            if self.encode(login, password) == token:
                return True
            else:
                return False

    tokenGenerator = Token()

    def __init__(self, profile: pymongo.collection.Collection):
        self.profileDB = profile
        self.router.add_api_route(self.route_str["reg"], self.registration, methods=["POST"])
        self.router.add_api_route(self.route_str["login"], self.login, methods=["POST"])

    def registration(
            self,
            firstName: str,
            lastName: str,
            email: EmailStr,
            password: str
    ):
        firstName = firstName.lower()
        lastName = lastName.lower()
        email = email.lower()
        data = Profile(
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=password
        )
        if self.profileDB.find_one({"email": email}) is None:
            self.profileDB.insert_one(data.dict())
            return HTTPException(status_code=201)

        elif self.profileDB.find_one({'email': email}):
            return HTTPException(status_code=409)

    def login(
            self,
            email: EmailStr,
            password: str
    ):
        data = self.profileDB.find_one({"email": email.lower()})
        if data is None:
            return HTTPException(status_code=404)
        elif data["password"] == password:
            return self.tokenGenerator.encode(data["email"], data["password"])
        else:
            return False


user = User(dbo.profile)
router = user.router
