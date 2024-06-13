from komgapy.response_classes import KomgaItem


class KomgaReadlist(KomgaItem):
    def __init__(self, readlist_data: dict) -> None:
        super().__init__(readlist_data)
        self.summary: str = readlist_data['summary']
        self.ordered: bool = readlist_data['ordered']
        self.book_ids: list = readlist_data['bookIds']


