from komgapy.response_classes import KomgaResponse

class KomgaItem(KomgaResponse):
    def __init__(self, item_data: dict) -> None:
        self.name: str = item_data['name']        
        self.id: str = item_data['id']

