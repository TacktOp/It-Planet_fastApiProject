from pydantic import BaseModel
from pydantic import EmailStr

from .PydanticObjectId import PydanticObjectId

class Profile(BaseModel):
    id: PydanticObjectId = None
    firstName: str
    lastName: str
    email: EmailStr
    password: str

class Locations(BaseModel):
    id: PydanticObjectId = None
    latitude: float
    longitude: float

class AnimalType(BaseModel):
    id: PydanticObjectId = None
    type: str