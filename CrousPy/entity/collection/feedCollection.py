from ..feed import Feed


class Feeds:
    """
    Représente une collection de flux régionaux.

    :param data: Les données des flux.
    :type data: dict

    :ivar feeds: Les flux.
    :vartype feeds: list[Feed]
    """

    def __init__(self, data: dict) -> None:
        self._data: dict = data

        self._feeds: list[Feed] = [Feed(feed) for feed in data]

    @property
    def data(self) -> dict:
        return self._data

    @property
    def feeds(self) -> list[Feed]:
        return self._feeds

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        if self.index >= len(self.feeds) - 1:
            raise StopIteration

        self.index += 1

        return self.feeds[self.index]

    def __getitem__(self, index: int) -> Feed:
        return self.feeds[index]

    def __len__(self) -> int:
        return len(self.feeds)

    def __repr__(self) -> str:
        return f"<Feeds feeds={self.feeds}>"
