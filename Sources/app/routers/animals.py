from fastapi import APIRouter
from pydantic import EmailStr

from ..database.database import Database

router = APIRouter()
dbo = Database()

