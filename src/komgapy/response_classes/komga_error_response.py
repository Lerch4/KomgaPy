from komgapy.response_classes import KomgaResponse

class KomgaErrorResponse(KomgaResponse):
    def __init__(self, response: dict) -> None:
        self.timestamp = response['timestamp']
        self.status_code = response['status']
        self.error = response['error']
        self.message = response['message']
        self.path = response['path']


