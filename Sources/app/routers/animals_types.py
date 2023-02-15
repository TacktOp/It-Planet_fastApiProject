from fastapi import APIRouter

from ..database.database import Database

router = APIRouter()
dbo = Database()

@router.get('/animals/types/{typeId}')
async def get_animalsTypes(
    typeId: int
):
    return

@router.post('/animals/types')
async def post_animalsTypes(
    type: str
):
    return

@router.put('/animals/types/{typeId}')
async def put_animalsTypes(
        typeId: int
):
    return

@router.delete('/animals/types/{typeId}')
async def delete_animalsTypes(
    typeId: int
):
    return