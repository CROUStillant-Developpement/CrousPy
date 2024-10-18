from typing import TypedDict


class DishData(TypedDict):
    """
    Définit la structure des données d'un plat.
    
    :param name: Le nom du plat.
    :type name: str
    """
    name: str


class Dish:
    """
    Représente un plat.
    
    :param data: Les données du plat.
    :type data: dict
    
    :ivar name: Le nom du plat.
    :vartype name: str
    """
    def __init__(self, data: DishData) -> None:
        self.__data: dict = data


    @property
    def data(self) -> dict:
        return self.__data
    
    @property
    def name(self) -> str:
        name: str = str(self.__data.get("name")).strip()

        if name.startswith("-"):
            name = name[1:].strip()
        elif name.startswith("*") or len(name) == 1 or name == "ou":
            name = ""
            
        if name.endswith(".") or name.endswith(","):
            name = name[:-1].strip()
            
        if "  " in name:
            name = name.replace("  ", " ")

        if not name.lower().startswith("ou"):
            name = name.capitalize()

        return name


    def __repr__(self) -> str:
        return f"<Dish name={self.name}>"
