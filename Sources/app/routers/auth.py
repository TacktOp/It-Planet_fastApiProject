from fastapi import APIRouter
from pydantic import EmailStr

from ..database.database import Database

router = APIRouter()
dbo = Database()

@router.post('/registration')
async def registration(
    firstName: str,
    lastName:str,
    email: EmailStr,
    password: str
):
    return dbo.add_profile(firstName=firstName,
                           lastName=lastName,
                           email=email,
                           password=password
                           )
