from fastapi import APIRouter
from pydantic import EmailStr

from ..database.operations import Operations

router = APIRouter()
dbo = Operations()

@router.get('/locations/{pointId}')
async def get_location(
    pointId:  int
):
    return

@router.post('/locations')
async def post_location(
     latitude: float,
	 longitude: float
):
    return

@router.put('/locations/{pointId}')
async def put_location(
    pointId: int
):
    return

@router.delete('/locations/{pointId}')
async def delete_location(
        pointId: int
):
    return