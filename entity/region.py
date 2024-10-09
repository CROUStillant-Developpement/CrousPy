from typing import TypedDict


class RegionData(TypedDict):
    """
    Définit la structure des données d'une région.
    
    :param code: Le code de la région.
    :type code: str

    :param id: L'ID de la région.
    :type id: int

    :param name: Le nom de la région.
    :type name: str
    """
    code: str
    id: int
    name: str


class Region:
    """
    Représente une région.
    
    :param data: Les données de la région.
    :type data: dict

    :ivar data: Les données de la région.
    :vartype data: dict

    :ivar code: Le code de la région.
    :vartype code: str

    :ivar id: L'ID de la région.
    :vartype id: int
    
    :ivar name: Le nom de la région.
    :vartype name: str
    """
    def __init__(self, data: RegionData) -> None:
        self.__data: dict = data


    @property
    def data(self) -> dict:
        return self.__data

    @property
    def code(self) -> str:
        return self.__data.get("code")

    @property
    def id(self) -> int:
        return self.__data.get("id")

    @property
    def name(self) -> str:
        return str(self.__data.get("name")).capitalize()
    

    def __repr__(self) -> str:
        return f"<Region name={self.name} id={self.id} code={self.code}>"
