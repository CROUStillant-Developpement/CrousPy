from . import __headers__, __baseURL__
from .entity.collection.regionCollection import Regions
from .entity.collection.ruCollection import RUs
from .entity.collection.menuCollection import Menus
from .entity.region import Region
from .entity.ru import RU
from .entity.menu import Menu
from .exceptions import *
from aiohttp import ClientSession, ContentTypeError


class Crous:
    def __init__(self, session: ClientSession):
        self.session = session


    async def getRegions(self) -> Regions:
        """
        Récupère les régions disponibles.
        
        :return: Les régions disponibles.
        :rtype: Regions

        :raises CrousAPIError: Une erreur est survenue.
        :raises RedirectError: Redirection !
        :raises BadRequestError: Mauvaise requête !
        :raises ForbiddenError: Accès refusé !
        :raises RegionIntrouvable: Cette région est introuvable !
        :raises ConflictWithServer: Conflit avec le serveur !
        :raises TooEarlyError: Trop tôt !
        :raises InternalServerError: Erreur interne du serveur !
        """
        try:
            async with self.session.get(f"{__baseURL__}/regions/", headers=__headers__, ssl=False) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    if response.status == 302:
                        raise RedirectError()
                    elif response.status == 400:
                        raise BadRequestError()
                    elif response.status == 403:
                        raise ForbiddenError()
                    elif response.status == 404:
                        raise RegionIntrouvable()
                    elif response.status == 409:
                        raise ConflictWithServer()
                    elif response.status == 425:
                        raise TooEarlyError()
                    elif response.status >= 500 and response.status < 600:
                        raise InternalServerError()
                    else:
                        raise CrousAPIError(json["message"])
                else:
                    return Regions(json)
        except ContentTypeError:
            raise CrousAPIError


    async def getRegionByID(self, regionID: int) -> Region:
        """
        Récupère une région par son ID.
        
        :param regionID: L'ID de la région.
        :type regionID: int
        
        :return: La région.
        :rtype: Region

        :raises CrousAPIError: Une erreur est survenue.
        :raises RedirectError: Redirection !
        :raises BadRequestError: Mauvaise requête !
        :raises ForbiddenError: Accès refusé !
        :raises RegionIntrouvable: Cette région est introuvable !
        :raises ConflictWithServer: Conflit avec le serveur !
        :raises TooEarlyError: Trop tôt !
        :raises InternalServerError: Erreur interne du serveur !
        """
        try:
            async with self.session.get(f"{__baseURL__}/regions/", headers=__headers__, ssl=False) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    if response.status == 302:
                        raise RedirectError()
                    elif response.status == 400:
                        raise BadRequestError()
                    elif response.status == 403:
                        raise ForbiddenError()
                    elif response.status == 404:
                        raise RegionIntrouvable()
                    elif response.status == 409:
                        raise ConflictWithServer()
                    elif response.status == 425:
                        raise TooEarlyError()
                    elif response.status >= 500 and response.status < 600:
                        raise InternalServerError()
                    else:
                        raise CrousAPIError(json["message"])
                else:
                    for region in json:
                        if region.get("id") == regionID:
                            return Region(region)
                    raise RegionIntrouvable()
        except ContentTypeError:
            raise CrousAPIError


    async def getRUs(self, regionID: int) -> RUs:
        """
        Récupère les RUs d'une région.
        
        :param regionID: L'ID de la région.
        :type regionID: int
        
        :return: Les RUs de la région.
        :rtype: RUs

        :raises CrousAPIError: Une erreur est survenue.
        :raises RedirectError: Redirection !
        :raises BadRequestError: Mauvaise requête !
        :raises ForbiddenError: Accès refusé !
        :raises RegionIntrouvable: Cette région est introuvable !
        :raises ConflictWithServer: Conflit avec le serveur !
        :raises TooEarlyError: Trop tôt !
        :raises InternalServerError: Erreur interne du serveur !
        """
        try:
            async with self.session.get(f"{__baseURL__}/regions/{regionID}/restaurants/", headers=__headers__, ssl=False) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    if response.status == 302:
                        raise RedirectError()
                    elif response.status == 400:
                        raise BadRequestError()
                    elif response.status == 403:
                        raise ForbiddenError()
                    elif response.status == 404:
                        raise RestaurantIntrouvable()
                    elif response.status == 409:
                        raise ConflictWithServer()
                    elif response.status == 425:
                        raise TooEarlyError()
                    elif response.status >= 500 and response.status < 600:
                        raise InternalServerError()
                    else:
                        raise CrousAPIError(json["message"])
                else:
                    return RUs(json)
        except ContentTypeError:
            raise CrousAPIError
        
    
    async def getRuByID(self, regionID: int, rid: int) -> RU:
        """
        Récupère un RU par son ID.
        
        :param regionID: L'ID de la région.
        :type regionID: int
        
        :param rid: L'ID du RU.
        :type rid: int
        
        :return: Le RU.
        :rtype: RU

        :raises CrousAPIError: Une erreur est survenue.
        :raises RedirectError: Redirection !
        :raises BadRequestError: Mauvaise requête !
        :raises ForbiddenError: Accès refusé !
        :raises RestaurantIntrouvable: Ce restaurant est introuvable !
        :raises ConflictWithServer: Conflit avec le serveur !
        :raises TooEarlyError: Trop tôt !
        :raises InternalServerError: Erreur interne du serveur !
        """
        try:
            async with self.session.get(f"{__baseURL__}/regions/{regionID}/restaurants/", headers=__headers__, ssl=False) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    if response.status == 302:
                        raise RedirectError()
                    elif response.status == 400:
                        raise BadRequestError()
                    elif response.status == 403:
                        raise ForbiddenError()
                    elif response.status == 404:
                        raise RestaurantIntrouvable()
                    elif response.status == 409:
                        raise ConflictWithServer()
                    elif response.status == 425:
                        raise TooEarlyError()
                    elif response.status >= 500 and response.status < 600:
                        raise InternalServerError()
                    else:
                        raise CrousAPIError(json["message"])
                else:
                    for ru in json:
                        if ru.get("id") == rid:
                            return RU(ru)
                    raise RestaurantIntrouvable()
        except ContentTypeError:
            raise CrousAPIError
        

    async def getMenus(self, regionID: int, rid: int) -> Menus:
        """
        Récupère les menus d'un RU.
        
        :param regionID: L'ID de la région.
        :type regionID: int
        
        :param rid: L'ID du RU.
        :type rid: int
        
        :return: Les menus du RU.
        :rtype: Menus

        :raises CrousAPIError: Une erreur est survenue.
        :raises RedirectError: Redirection !
        :raises BadRequestError: Mauvaise requête !
        :raises ForbiddenError: Accès refusé !
        :raises ConflictWithServer: Conflit avec le serveur !
        :raises TooEarlyError: Trop tôt !
        :raises InternalServerError: Erreur interne du serveur !
        """
        try:
            async with self.session.get(f"{__baseURL__}/regions/{regionID}/restaurants/{rid}/menus/", headers=__headers__, ssl=False) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    if response.status == 302:
                        raise RedirectError()
                    elif response.status == 400:
                        raise BadRequestError()
                    elif response.status == 403:
                        raise ForbiddenError()
                    elif response.status == 404:
                        raise MenuIntrouvable()
                    elif response.status == 409:
                        raise ConflictWithServer()
                    elif response.status == 425:
                        raise TooEarlyError()
                    elif response.status >= 500 and response.status < 600:
                        raise InternalServerError()
                    else:
                        raise CrousAPIError(json["message"])
                else:
                    return Menus(json)
        except ContentTypeError:
            raise CrousAPIError
        

    async def getMenuByDate(self, regionID: int, rid: int, date: str) -> Menu:
        """
        Récupère un menu par sa date.
        
        :param regionID: L'ID de la région.
        :type regionID: int
        
        :param rid: L'ID du RU.
        :type rid: int
        
        :param date: La date.
        :type date: str
        
        :return: Le menu.
        :rtype: Menu

        :raises CrousAPIError: Une erreur est survenue.
        :raises RedirectError: Redirection !
        :raises BadRequestError: Mauvaise requête !
        :raises ForbiddenError: Accès refusé !
        :raises MenuIntrouvable: Le menu n'est pas disponible !
        :raises ConflictWithServer: Conflit avec le serveur !
        :raises TooEarlyError: Trop tôt !
        :raises InternalServerError: Erreur interne du serveur !
        """
        try:
            async with self.session.get(f"{__baseURL__}/regions/{regionID}/restaurants/{rid}/menus/", headers=__headers__, ssl=False) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    if response.status == 302:
                        raise RedirectError()
                    elif response.status == 400:
                        raise BadRequestError()
                    elif response.status == 403:
                        raise ForbiddenError()
                    elif response.status == 404:
                        raise MenuIntrouvable()
                    elif response.status == 409:
                        raise ConflictWithServer()
                    elif response.status == 425:
                        raise TooEarlyError()
                    elif response.status >= 500 and response.status < 600:
                        raise InternalServerError()
                    else:
                        raise CrousAPIError(json["message"])
                else:
                    for menu in json:
                        if menu.get("date") == date:
                            return Menu(menu)
                    raise MenuIntrouvable()
        except ContentTypeError:
            raise CrousAPIError
