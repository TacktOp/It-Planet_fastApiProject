from fastapi import APIRouter

from ..database.database import Database

router = APIRouter()
dbo = Database()


@router.get('/locations/{pointId}')
async def get_location(
        pointId: str
):
    return Database().location_get(pointId=pointId)


@router.post('/locations')
async def post_location(
        latitude: float,
        longitude: float
):
    return Database().location_post(
        latitude=latitude,
        longitude=longitude
    )


@router.put('/locations/{pointId}')
async def put_location(
        pointId: str,
        latitude: float,
        longitude: float
):
    return Database().location_put(
        pointId=pointId,
        latitude=latitude,
        longitude=longitude
    )


@router.delete('/locations/{pointId}')
async def delete_location(
        pointId: str
):
    return Database().location_delete(pointId=pointId)
