from aiohttp import ClientSession
from async_timeout import timeout

from .entity.collection.feedCollection import Feeds
from .entity.collection.feedRuCollection import FeedRUs
from .entity.collection.menuCollection import Menus
from .entity.collection.regionCollection import Regions
from .entity.collection.ruCollection import RUs
from .entity.menu import Menu as ObjMenu
from .entity.region import Region as ObjRegion
from .entity.ru import RU as ObjRU
from .exceptions import CrousAPIError
from .requests import Crous as CrousRequests

timeout_time = 30


class Crous:
    """
    Représente le client Crous.

    :param session: La session aiohttp.
    :type session: ClientSession

    :ivar region: Les régions.
    :vartype region: Region

    :ivar ru: Les restaurants universitaires.
    :vartype ru: RU

    :ivar menu: Les menus.
    :vartype menu: Menu

    :ivar feed: Les flux régionaux.
    :vartype feed: Feed

    :ivar image: Les images.
    :vartype image: Image

    :raises CrousAPIError: Une erreur est survenue lors de la requête.
    :raises asyncio.TimeoutError: La requête a mis trop de temps à répondre.
    """

    def __init__(self, session: ClientSession):
        self.client = CrousRequests(session)

        self.region = Region(self.client)
        self.ru = RU(self.client)
        self.menu = Menu(self.client)
        self.feed = Feed(self.client)
        self.image = Image(self.client)


class Region:
    """
    Représente les régions.

    :param client: Le client Crous.
    :type client: CrousRequests

    :method get: Récupère les régions.
    :method getById: Récupère une région par son ID.

    :raises CrousAPIError: Une erreur est survenue lors de la requête.
    :raises asyncio.TimeoutError: La requête a mis trop de temps à répondre.
    """

    def __init__(self, client: CrousRequests):
        self.client = client

    async def get(self) -> Regions:
        try:
            async with timeout(timeout_time):
                return await self.client.getRegions()
        except TimeoutError:
            raise CrousAPIError

    async def getById(self, regionID: int) -> ObjRegion:
        try:
            async with timeout(timeout_time):
                return await self.client.getRegionByID(regionID)
        except TimeoutError:
            raise CrousAPIError


class RU:
    """
    Représente les restaurants universitaires.

    :param client: Le client Crous.
    :type client: CrousRequests

    :method get: Récupère les restaurants universitaires.
    :method getById: Récupère un restaurant universitaire par son ID.

    :raises CrousAPIError: Une erreur est survenue lors de la requête.
    :raises asyncio.TimeoutError: La requête a mis trop de temps à répondre.
    """

    def __init__(self, client: CrousRequests):
        self.client = client

    async def get(self, regionID: int) -> RUs:
        try:
            async with timeout(timeout_time):
                return await self.client.getRUs(regionID)
        except TimeoutError:
            raise CrousAPIError

    async def getById(self, regionID: int, rid: int) -> ObjRU:
        try:
            async with timeout(timeout_time):
                return await self.client.getRuByID(regionID, rid)
        except TimeoutError:
            raise CrousAPIError


class Menu:
    """
    Représente les menus.

    :param client: Le client Crous.
    :type client: CrousRequests

    :method get: Récupère les menus.
    :method getByName: Récupère un menu par son nom.

    :raises CrousAPIError: Une erreur est survenue lors de la requête.
    :raises asyncio.TimeoutError: La requête a mis trop de temps à répondre.
    """

    def __init__(self, client: CrousRequests):
        self.client = client

    async def get(self, regionID: int, rid: str) -> Menus:
        try:
            async with timeout(timeout_time):
                return await self.client.getMenus(regionID, rid)
        except TimeoutError:
            raise CrousAPIError

    async def getByDate(self, regionID: int, rid: str, date: str) -> ObjMenu:
        try:
            async with timeout(timeout_time):
                return await self.client.getMenuByDate(regionID, rid, date)
        except TimeoutError:
            raise CrousAPIError


class Feed:
    """
    Représente les flux régionaux.

    Chaque flux contient tous les restaurants d'une région et leurs menus. Les flux
    sont régénérés toutes les 15 minutes par le CROUS, même sans changement.

    :param client: Le client Crous.
    :type client: CrousRequests

    :method get: Récupère la liste des flux régionaux.
    :method getByURL: Récupère un flux régional.

    :raises CrousAPIError: Une erreur est survenue lors de la requête.
    :raises asyncio.TimeoutError: La requête a mis trop de temps à répondre.
    """

    def __init__(self, client: CrousRequests):
        self.client = client

    async def get(self) -> Feeds:
        try:
            async with timeout(timeout_time):
                return await self.client.getFeeds()
        except TimeoutError:
            raise CrousAPIError

    async def getByURL(self, url: str) -> FeedRUs:
        try:
            async with timeout(timeout_time):
                return await self.client.getFeed(url)
        except TimeoutError:
            raise CrousAPIError


class Image:
    """
    Représente les images des restaurants.

    :param client: Le client Crous.
    :type client: CrousRequests

    :method get: Récupère le contenu brut d'une image.

    :raises CrousAPIError: Une erreur est survenue lors de la requête.
    :raises asyncio.TimeoutError: La requête a mis trop de temps à répondre.
    """

    def __init__(self, client: CrousRequests):
        self.client = client

    async def get(self, url: str) -> bytes:
        try:
            async with timeout(timeout_time):
                return await self.client.getImage(url)
        except TimeoutError:
            raise CrousAPIError
