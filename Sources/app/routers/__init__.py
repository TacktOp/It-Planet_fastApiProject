from .animals import router as animals_router
from .animals_types import router as animalsTypes_router
from .animals_locations import router as animalsLocations_router
from .accounts import router as accounts_router
from .locations import router as locations_router
from .auth import User, get_profile

RouterApi = User(get_profile())