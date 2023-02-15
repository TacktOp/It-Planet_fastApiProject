from fastapi import APIRouter
from pydantic import EmailStr

from ..database.database import Database

router = APIRouter()
dbo = Database()

@router.get('/accounts/{accountId}')
async def get_account(
    accountId: int
):
    return

@router.get('/accounts/search')
async def get_accounts(
    firstName: str,
    lastName: str,
    email: EmailStr,
    fromm: int,
    size: int
):
    return

@router.put('/accounts/{accountId}')
async def put_account(
    accountId: int
):
    return

@router.delete('/accounts/{accountId}')
async def delete_account(
    accountId: int
):
    return