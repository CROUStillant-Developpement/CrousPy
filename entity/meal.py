from .category import Category
from typing import TypedDict, Literal


class MealData(TypedDict):
    """
    Définit la structure des données d'un repas.
    
    :param name: Le nom du repas.
    :type name: str
    
    :param foodcategory: Les catégories.
    :type foodcategory: list[dict]
    """
    name: str
    foodcategory: list[Category]


class Meal:
    """
    Représente un repas.
    
    :param data: Les données du repas.
    :type data: dict

    :ivar name: Le nom du repas.
    :vartype name: str[matin, midi, soir]

    :ivar categories: Les catégories de nourriture.
    :vartype categories: list[Category]
    """
    def __init__(self, data: MealData) -> None:
        self.__data: dict = data


    @property
    def data(self) -> dict:
        return self.__data

    @property
    def name(self) -> Literal['matin', 'midi', 'soir']:
        return str(self.__data.get("name")).lower()
    
    @property
    def categories(self) -> list[Category]:
        return [Category(category) for category in self.__data.get("foodcategory")]


    def __iter__(self):
        self.index = -1
        return self
    

    def __next__(self):
        if self.index >= len(self.categories) - 1:
            raise StopIteration

        self.index += 1

        return self.categories[self.index]
    

    def __getitem__(self, index: int) -> Category:
        return self.categories[index]
    

    def __len__(self) -> int:
        return len(self.categories)
    

    def __repr__(self) -> str:
        return f"<Meal name={self.name} categories={self.categories}>"
