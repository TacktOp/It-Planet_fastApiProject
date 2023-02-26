from fastapi import APIRouter
from pydantic import EmailStr

from ..database.database import Database

router = APIRouter()
dbo = Database()

@router.get('/account/{accountId}')
async def get_account(
    accountId: str
):
    return Database().account_get(accountId=accountId)

@router.get('/accounts/search')
async def get_account_search(
    firstName: str = None,
    lastName: str = None,
    email: EmailStr = None,
    fromm: int = 0,
    size: int = 10
):
    return Database().account_search_get(firstName=firstName,
                                         lastName=lastName,
                                         email=email,
                                         fromm=fromm,
                                         size=size
                                         )

@router.put('/accounts/{accountId}')
async def put_account(
    accountId: str,
    firstName: str,
    lastName: str,
    email: EmailStr,
    password: str
):
    return Database().account_put(accountId=accountId,
                                  firstName=firstName,
                                  lastName=lastName,
                                  email=email,
                                  password=password
                                  )

@router.delete('/accounts/{accountId}')
async def delete_account(
    accountId: str
):
    return Database().account_delete(accountId=accountId)