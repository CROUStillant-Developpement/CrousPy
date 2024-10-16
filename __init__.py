__title__ = "CrousPy"
__author__ = "CROUStillant Développement"
__version__ = "2.0.2"
__description__ = "A Python wrapper for the CROUS API."

__headers__ = {
    "User-Agent": f"CrousPy v{__version__} - https://github.com/CROUStillant-Developpement"
}

__baseURL__ = "https://webservices-v2.crous-mobile.fr/ws/v1"


from .client import Crous

# Regions
from .entity.region import Region
from .entity.collection.regionCollection import Regions

# Restaurants Universitaires
from .entity.ru import RU
from .entity.collection.ruCollection import RUs

# Menus
from .entity.menu import Menu
from .entity.collection.menuCollection import Menus

# Meal
from .entity.meal import Meal

# Categories
from .entity.category import Category

# Dishes
from .entity.dish import Dish

# Exceptions
from .exceptions import *
