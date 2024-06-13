from komgapy.response_classes import KomgaItem

class KomgaCollection(KomgaItem):
    def __init__(self, collection_data: dict) -> None:
        super().__init__(collection_data)
        self.ordered: bool = collection_data['ordered']
        self.series_ids: list = collection_data['seriesIds']
        self.created_date = collection_data['createdDate']


