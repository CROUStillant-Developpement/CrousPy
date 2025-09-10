from ..ru import RU


class RUs:
    """
    Une collection de RU.

    :ivar data: Les données.
    :vartype data: dict

    :ivar rus: Les RU.
    :vartype rus: list[RU]
    """

    def __init__(self, data: dict) -> None:
        self._data: dict = data

        self._rus: list = [RU(ru) for ru in data]

    @property
    def data(self) -> dict:
        return self._data

    @property
    def rus(self) -> list:
        return self._rus

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index >= len(self.rus) - 1:
            raise StopIteration

        self.index += 1

        return self.rus[self.index]

    def __getitem__(self, index: int) -> RU:
        return self.rus[index]

    def __len__(self) -> int:
        return len(self.rus)

    def __repr__(self) -> str:
        return f"<RUs rus={self.rus}>"
