from ..menu import Menu


class Menus:
    """
    Représente une collection de menus.
    
    :param data: Les données des menus.
    :type data: dict
    
    :ivar menus: Les menus.
    :vartype menus: list[Menu]
    """
    def __init__(self, data: dict) -> None:
        self._data: dict = data

        self._menus: list[Menu] = [Menu(menu) for menu in data]


    def getByDate(self, date: str) -> Menu:
        """
        Récupère un menu par sa date.
        
        :param date: La date du menu.
        :type date: str
        
        :return: Menu
        :rtype: Menu
        """
        for menu in self.menus:
            if menu.date.strftime("%Y-%m-%d") == date:
                return menu

        return None


    @property
    def data(self) -> dict:
        return self._data
    
    @property
    def menus(self) -> list[Menu]:
        return self._menus


    def __iter__(self):
        self.index = -1
        return self
    

    def __next__(self):
        if self.index >= len(self.menus) - 1:
            raise StopIteration

        self.index += 1

        return self.menus[self.index]
    

    def __getitem__(self, index: int) -> Menu:
        return self.menus[index]
    

    def __len__(self) -> int:
        return len(self.menus)
    

    def __repr__(self) -> str:
        return f"<Menus menus={self.menus}>"
