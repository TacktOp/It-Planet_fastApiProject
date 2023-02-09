from fastapi import APIRouter
from pydantic import EmailStr

from ..database.operations import Operations

router = APIRouter()
dbo = Operations()

@router.post('/registration')
async def registration(
    firstName: str,
    lastName:str,
    email: EmailStr,
    password:str
):
    return
