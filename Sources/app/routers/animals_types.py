from fastapi import APIRouter

from ..database.database import Database

router = APIRouter()
dbo = Database()

@router.get('/animals/types/{typeId}')
async def get_animals_types(
    typeId: str
):
    return Database().animal_type_get(typeId=typeId)

@router.post('/animals/types')
async def post_animals_types(
    type: str
):
    return Database().animal_type_post(type=type)

@router.put('/animals/types/{typeId}')
async def put_animals_types(
        typeId: str,
        type: str
):
    return Database().animal_type_put(typeId=typeId, type=type)

@router.delete('/animals/types/{typeId}')
async def delete_animals_types(
    typeId: str
):
    return Database().animal_type_delete(typeId=typeId)
