from .dish import Dish
from typing import TypedDict


class CategoryData(TypedDict):
    """
    Définit la structure des données d'une catégorie de nourriture.

    :param name: Le nom de la catégorie de nourriture.
    :type name: str

    :param dishes: Les plats.
    :type dishes: list[dict]
    """

    name: str
    dishes: list[Dish]


class Category:
    """
    Représente une catégorie de nourriture.

    :param data: Les données de la catégorie de nourriture.
    :type data: dict

    :ivar name: Le nom de la catégorie de nourriture.
    :vartype name: str

    :ivar dishes: Les plats.
    :vartype dishes: list[Dish]
    """

    def __init__(self, data: CategoryData) -> None:
        self.__data: dict = data

    @property
    def data(self) -> dict:
        return self.__data

    @property
    def name(self) -> str:
        return str(self.__data.get("name")).capitalize()

    @property
    def dishes(self) -> list[Dish]:
        return [
            Dish(dish)
            for dish in self.__data.get("dishes")
            if dish.get("name").strip() != ""
        ]

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index >= len(self.dishes) - 1:
            raise StopIteration

        self.index += 1

        return self.dishes[self.index]

    def __getitem__(self, index: int) -> Dish:
        return self.dishes[index]

    def __len__(self) -> int:
        return len(self.dishes)

    def __repr__(self) -> str:
        return f"<Category name={self.name} dishes={self.dishes}>"
