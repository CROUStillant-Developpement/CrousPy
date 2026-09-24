from typing import TypedDict


class FeedData(TypedDict):
    """
    Définit la structure des données d'un flux régional.

    :param id: L'ID du flux.
    :type id: int

    :param name: Le nom du flux.
    :type name: str

    :param url: L'URL du flux.
    :type url: str

    :param is_default: Si le flux est le flux par défaut.
    :type is_default: bool
    """

    id: int
    name: str
    url: str
    is_default: bool


class Feed:
    """
    Représente un flux régional (un fichier JSON contenant tous les restaurants
    d'une région et leurs menus, régénéré toutes les 15 minutes par le CROUS).

    :param data: Les données du flux.
    :type data: dict

    :ivar data: Les données du flux.
    :vartype data: dict

    :ivar id: L'ID du flux (différent de l'ID de la région).
    :vartype id: int

    :ivar name: Le nom du flux.
    :vartype name: str

    :ivar url: L'URL du flux.
    :vartype url: str
    """

    def __init__(self, data: FeedData) -> None:
        self.__data: dict = data

    @property
    def data(self) -> dict:
        return self.__data

    @property
    def id(self) -> int:
        return self.__data.get("id")

    @property
    def name(self) -> str:
        return str(self.__data.get("name")).strip()

    @property
    def url(self) -> str:
        return self.__data.get("url")

    def __repr__(self) -> str:
        return f"<Feed name={self.name} id={self.id}>"
