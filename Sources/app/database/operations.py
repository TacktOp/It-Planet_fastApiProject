from pydantic import EmailStr

from .database import Database
from ..models.models import Profile

class Operations:

    def add_profile(
        selfs,
        firstName: str,
        lastName:str,
        email: EmailStr,
        password:str
        ):
        data = Profile(
        firstName=firstName,
        lastName=lastName,
        email=email,
        password=password
        )
        for data in data:
            pass
