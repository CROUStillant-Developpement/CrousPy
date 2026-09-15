__title__ = "CrousPy"
__author__ = "CROUStillant Développement"
__version__ = "2.0.7"
__description__ = "A Python wrapper for the CROUS API."

__headers__ = {
    "User-Agent": f"CrousPy v{__version__} - https://github.com/CROUStillant-Developpement"
}

__baseURL__ = "https://webservices-v2.crous-mobile.fr/ws/v1"


from .client import Crous

# Categories
from .entity.category import Category
from .entity.collection.menuCollection import Menus
from .entity.collection.regionCollection import Regions
from .entity.collection.ruCollection import RUs

# Dishes
from .entity.dish import Dish

# Meal
from .entity.meal import Meal

# Menus
from .entity.menu import Menu

# Regions
from .entity.region import Region

# Restaurants Universitaires
from .entity.ru import RU

# Exceptions
from .exceptions import (
    BadRequestError,
    ConflictWithServer,
    CrousAPIError,
    ForbiddenError,
    InternalServerError,
    MenuIntrouvable,
    RedirectError,
    RegionIntrouvable,
    RestaurantIntrouvable,
    TeapotError,
    TooEarlyError,
)

__all__ = [
    "RU",
    "BadRequestError",
    "Category",
    "ConflictWithServer",
    "Crous",
    "CrousAPIError",
    "Dish",
    "ForbiddenError",
    "InternalServerError",
    "Meal",
    "Menu",
    "MenuIntrouvable",
    "Menus",
    "RUs",
    "RedirectError",
    "Region",
    "RegionIntrouvable",
    "Regions",
    "RestaurantIntrouvable",
    "TeapotError",
    "TooEarlyError",
]
