from fastapi import APIRouter
from pydantic import EmailStr
from datetime import datetime

from ..database.database import Database

router = APIRouter()
dbo = Database()

@router.get('/animals/{animalId}/locations')
async def get_animalLocations(
    animalId: int,
    startDateTime: datetime,
    endDateTime: datetime,
    fromm: int,
    size: int
):
    return

@router.post('/animals/{animalId}/locations/{pointId}')
async def post_animalLocations(
    animalId: int,
    pointId: int
):
    return

@router.put('/animals/{animalId}/locations')
async def put_animalLocations(
    animalId: int
):
    return

@router.delete('/animals/{animalId}/locations/{visitedPointId}')
async def delete_animalLocations(
    animalId: int,
    visitedPointId: int
):
    return