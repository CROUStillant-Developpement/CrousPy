from typing import TypedDict

from ..utils import formatTitle
from .collection.menuCollection import Menus


class FeedRUData(TypedDict):
    """
    Définit la structure des données d'un RU dans un flux régional.

    :param id: L'ID du RU dans le flux (différent de l'ID de l'API, voir ``RU.feedId``).
    :type id: int

    :param title: Le titre.
    :type title: str

    :param lat: La latitude.
    :type lat: float

    :param lon: La longitude.
    :type lon: float

    :param area: La zone.
    :type area: str

    :param adresse: L'adresse.
    :type adresse: str

    :param opening: Les jours d'ouverture.
    :type opening: str

    :param closing: Si le RU est fermé.
    :type closing: str

    :param type: Le type.
    :type type: str

    :param menus: Les menus.
    :type menus: list[dict]
    """

    id: int
    title: str
    lat: float
    lon: float
    area: str
    adresse: str
    opening: str
    closing: str
    type: str
    menus: list[dict]


class FeedRU:
    """
    Représente un Restaurant Universitaire dans un flux régional.

    :param data: Les données du RU.
    :type data: dict

    :ivar data: Les données du RU.
    :vartype data: dict

    :ivar id: L'ID du RU dans le flux.
    :vartype id: int

    :ivar title: Le titre.
    :vartype title: str

    :ivar area: La zone.
    :vartype area: str

    :ivar opening: Les jours d'ouverture.
    :vartype opening: str

    :ivar closing: Si le RU est fermé.
    :vartype closing: str

    :ivar open: Si le RU est ouvert.
    :vartype open: bool

    :ivar menus: Les menus (les menus des flux n'ont pas d'ID, ``Menu.id`` vaut ``None``).
    :vartype menus: Menus
    """

    def __init__(self, data: FeedRUData) -> None:
        self.__data: dict = data

    @property
    def data(self) -> dict:
        return self.__data

    @property
    def id(self) -> int:
        return self.__data.get("id")

    @property
    def title(self) -> str:
        return formatTitle(self.__data.get("title"))

    @property
    def area(self) -> str:
        return self.__data.get("area")

    @property
    def opening(self) -> str:
        return self.__data.get("opening")

    @property
    def closing(self) -> str:
        return self.__data.get("closing")

    @property
    def open(self) -> bool:
        return self.__data.get("closing") == "0"

    @property
    def menus(self) -> Menus:
        return Menus(self.__data.get("menus") or [])

    def __repr__(self) -> str:
        return f"<FeedRU title={self.title} id={self.id}>"
