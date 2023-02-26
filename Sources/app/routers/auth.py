import base64
from typing import List

import pymongo
import uvicorn
from fastapi import APIRouter, FastAPI, Request, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import EmailStr
from pymongo import MongoClient
from starlette import status
from starlette.responses import JSONResponse

from ..models.models import Profile


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


def get_profile() -> pymongo.collection.Collection:
    CONNECTION_STRING = "mongodb://localhost:27017"
    client = MongoClient(CONNECTION_STRING)
    return client.get_database("it-planeta").get_collection("profile")


if __name__ == "__main__":
    RouterApi = User(get_profile())
    app = FastAPI()
    app.include_router(RouterApi.router)


    @app.middleware("http")
    async def add_process_time_header(request: Request, call_next):
        print(request.headers.get("Authorization"))
        for i in (RouterApi.route_str | {"docs": "/docs", "openapi": "/openapi.json"}).values():
            if i == request.url.path:
                response = await call_next(request)
                return response
        else:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content=jsonable_encoder({"detail": "Авторизация", "body": "вы не авторизованы"}),
            )


    uvicorn.run(app)
