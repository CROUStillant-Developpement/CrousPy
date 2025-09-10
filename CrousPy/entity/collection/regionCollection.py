from ..region import Region


class Regions:
    """
    Représente les régions.

    :param data: Les données des régions.
    :type data: dict

    :ivar regions: Les régions.
    :vartype regions: list[Region]
    """

    def __init__(self, data: dict) -> None:
        self._data: dict = data

        self._regions: list[Region] = [Region(region) for region in data]

    @property
    def data(self) -> dict:
        return self._data

    @property
    def regions(self) -> list[Region]:
        return self._regions

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index >= len(self.regions) - 1:
            raise StopIteration

        self.index += 1

        return self.regions[self.index]

    def __getitem__(self, index: int) -> Region:
        return self.regions[index]

    def __len__(self) -> int:
        return len(self.regions)

    def __repr__(self) -> str:
        return f"<Regions regions={self.regions}>"

    def getFromID(self, id: int) -> Region:
        """
        Récupère une région à partir de son ID.

        :param id: L'ID de la région.
        :type id: int

        :return: La région.
        :rtype: Region
        """
        for ru in self.regions:
            if ru.id == id:
                return ru

        return None
