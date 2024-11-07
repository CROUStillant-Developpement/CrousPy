import pytz

from .meal import Meal
from typing import TypedDict
from datetime import datetime


class MenuData(TypedDict):
    """
    Définit la structure des données d'un menu.
    
    :param id: L'ID du menu.
    :type id: int
    
    :param restaurant_id: L'ID du restaurant.
    :type restaurant_id: int
    
    :param date: La date du menu.
    :type date: str
    
    :param meal: Le repas du menu.
    :type meal: list[dict]
    """
    id: int
    restaurant_id: int
    date: str
    meal: list[Meal]


class Menu:
    """
    Représente un menu.
    
    :param data: Les données du menu.
    :type data: dict
    
    :ivar data: Les données du menu.
    :vartype data: dict
    
    :ivar id: L'ID du menu.
    :vartype id: int
    
    :ivar restaurant_id: L'ID du restaurant.
    :vartype restaurant_id: int
    
    :ivar date: La date du menu.
    :vartype date: str
    
    :ivar meal: Le repas du menu.
    :vartype meal: list
    """
    def __init__(self, data: MenuData) -> None:
        self.__data: dict = data


    @property
    def data(self) -> dict:
        return self.__data

    @property
    def id(self) -> int:
        return self.__data.get("id")

    @property
    def restaurant_id(self) -> int:
        return self.__data.get("restaurant_id")

    @property
    def date(self) -> datetime:
        year, month, day = self.__data.get("date").split("-")
        return datetime(int(year), int(month), int(day), 0, 0, 0, tzinfo=pytz.timezone("Europe/Paris"))

    @property
    def meals(self) -> list[Meal]:
        return [Meal(meal) for meal in self.__data.get("meal")]


    def __iter__(self):
        self.index = -1
        return self


    def __next__(self):
        if self.index >= len(self.meals) - 1:
            raise StopIteration

        self.index += 1

        return self.meals[self.index]


    def __getitem__(self, index: int) -> Meal:
        return self.meals[index]


    def __len__(self) -> int:
        return len(self.meals)


    def __repr__(self) -> str:
        return f"<Menu id={self.id} restaurant_id={self.restaurant_id} date={self.date}>"
