from ..feedRu import FeedRU


class FeedRUs:
    """
    Une collection de RU issus d'un flux régional.

    :ivar data: Les données.
    :vartype data: dict

    :ivar rus: Les RU.
    :vartype rus: list[FeedRU]
    """

    def __init__(self, data: dict) -> None:
        self._data: dict = data

        self._rus: list[FeedRU] = [FeedRU(ru) for ru in data]

    @property
    def data(self) -> dict:
        return self._data

    @property
    def rus(self) -> list[FeedRU]:
        return self._rus

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index >= len(self.rus) - 1:
            raise StopIteration

        self.index += 1

        return self.rus[self.index]

    def __getitem__(self, index: int) -> FeedRU:
        return self.rus[index]

    def __len__(self) -> int:
        return len(self.rus)

    def __repr__(self) -> str:
        return f"<FeedRUs rus={self.rus}>"
