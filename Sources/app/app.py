from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from .routers import *

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, tags=['auth'])
app.include_router(accounts_router, tags=['accounts'])
app.include_router(locations_router, tags=['locations'])
app.include_router(animals_router, tags=['animals'])
app.include_router(animalsTypes_router, tags=['animals types'])
app.include_router(animalsLocations_router, tags=['animals locations'])
