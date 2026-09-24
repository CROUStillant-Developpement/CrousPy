from json import JSONDecodeError, loads

from aiohttp import ClientSession, ContentTypeError

from . import __baseURL__, __feedIndexURL__, __headers__
from .entity.collection.feedCollection import Feeds
from .entity.collection.feedRuCollection import FeedRUs
from .entity.collection.menuCollection import Menus
from .entity.collection.regionCollection import Regions
from .entity.collection.ruCollection import RUs
from .entity.menu import Menu
from .entity.region import Region
from .entity.ru import RU
from .exceptions import (
    BadRequestError,
    ConflictWithServer,
    CrousAPIError,
    FluxIntrouvable,
    ForbiddenError,
    InternalServerError,
    MenuIntrouvable,
    RedirectError,
    RegionIntrouvable,
    RestaurantIntrouvable,
    TooEarlyError,
)


def _raiseForStatus(status: int, json, notFound: type[CrousAPIError]) -> None:
    """
    Lève l'exception correspondant au code HTTP d'une réponse en erreur.

    :param status: Le code HTTP.
    :type status: int

    :param json: Le corps de la réponse (décodé).

    :param notFound: L'exception à lever en cas de 404.
    :type notFound: type[CrousAPIError]
    """
    if status == 302:
        raise RedirectError()
    elif status == 400:
        raise BadRequestError()
    elif status == 403:
        raise ForbiddenError()
    elif status == 404:
        raise notFound()
    elif status == 409:
        raise ConflictWithServer()
    elif status == 425:
        raise TooEarlyError()
    elif status >= 500 and status < 600:
        raise InternalServerError()
    else:
        raise CrousAPIError(json["message"])


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
            async with self.session.get(
                f"{__baseURL__}/regions/", headers=__headers__, ssl=False
            ) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    _raiseForStatus(response.status, json, RegionIntrouvable)
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
            async with self.session.get(
                f"{__baseURL__}/regions/", headers=__headers__, ssl=False
            ) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    _raiseForStatus(response.status, json, RegionIntrouvable)
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
        :raises RestaurantIntrouvable: Ce restaurant est introuvable !
        :raises ConflictWithServer: Conflit avec le serveur !
        :raises TooEarlyError: Trop tôt !
        :raises InternalServerError: Erreur interne du serveur !
        """
        try:
            async with self.session.get(
                f"{__baseURL__}/regions/{regionID}/restaurants/",
                headers=__headers__,
                ssl=False,
            ) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    _raiseForStatus(response.status, json, RestaurantIntrouvable)
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
            async with self.session.get(
                f"{__baseURL__}/regions/{regionID}/restaurants/",
                headers=__headers__,
                ssl=False,
            ) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    _raiseForStatus(response.status, json, RestaurantIntrouvable)
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
            async with self.session.get(
                f"{__baseURL__}/regions/{regionID}/restaurants/{rid}/menus/",
                headers=__headers__,
                ssl=False,
            ) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    _raiseForStatus(response.status, json, MenuIntrouvable)
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
            async with self.session.get(
                f"{__baseURL__}/regions/{regionID}/restaurants/{rid}/menus/",
                headers=__headers__,
                ssl=False,
            ) as response:
                json: list[dict] = await response.json()
                if response.status != 200:
                    _raiseForStatus(response.status, json, MenuIntrouvable)
                for menu in json:
                    if menu.get("date") == date:
                        return Menu(menu)
                raise MenuIntrouvable()
        except ContentTypeError:
            raise CrousAPIError

    async def _getFeedJSON(self, url: str) -> dict:
        """
        Récupère et décode un fichier JSON des flux.

        Certains flux contiennent des caractères de contrôle bruts (tabulations,
        retours à la ligne) dans les chaînes : ils sont décodés en mode non strict,
        ce qui donne exactement les mêmes chaînes que l'API.

        :param url: L'URL du fichier.
        :type url: str

        :return: Le JSON décodé.
        :rtype: dict

        :raises CrousAPIError: Une erreur est survenue.
        :raises FluxIntrouvable: Ce flux est introuvable !
        """
        async with self.session.get(url, headers=__headers__) as response:
            text = await response.text()
            if response.status != 200:
                _raiseForStatus(
                    response.status, {"message": text[:200]}, FluxIntrouvable
                )
        try:
            return loads(text, strict=False)
        except JSONDecodeError as e:
            raise CrousAPIError(f"Flux invalide ({url}) : {e}")

    async def getFeeds(self) -> Feeds:
        """
        Récupère la liste des flux régionaux.

        :return: Les flux régionaux.
        :rtype: Feeds

        :raises CrousAPIError: Une erreur est survenue.
        :raises FluxIntrouvable: Ce flux est introuvable !
        """
        json = await self._getFeedJSON(__feedIndexURL__)
        return Feeds(json.get("results") or [])

    async def getFeed(self, url: str) -> FeedRUs:
        """
        Récupère un flux régional : tous les RUs de la région et leurs menus.

        :param url: L'URL du flux (voir ``Feed.url``).
        :type url: str

        :return: Les RUs du flux.
        :rtype: FeedRUs

        :raises CrousAPIError: Une erreur est survenue.
        :raises FluxIntrouvable: Ce flux est introuvable !
        """
        json = await self._getFeedJSON(url)
        return FeedRUs(json.get("restaurants") or [])

    async def getImage(self, url: str) -> bytes:
        """
        Récupère le contenu brut d'une image.

        :param url: L'URL de l'image.
        :type url: str

        :return: Le contenu de l'image.
        :rtype: bytes

        :raises CrousAPIError: Une erreur est survenue.
        """
        async with self.session.get(url, headers=__headers__) as response:
            content = await response.read()
            if response.status != 200:
                _raiseForStatus(
                    response.status,
                    {"message": f"HTTP {response.status}"},
                    CrousAPIError,
                )
            return content
