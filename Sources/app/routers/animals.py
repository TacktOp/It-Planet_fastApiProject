from fastapi import APIRouter

from ..database.operations import Operations

router = APIRouter()
dbo = Operations()

