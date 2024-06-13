from komgapy.response_classes.komga_response import KomgaResponse
from komgapy.convert_response_util import convert_item_list_to_objects


class KomgaSearchResponse(KomgaResponse):
    def __init__(self, komga_search_response: dict) -> None:

        self.content = convert_item_list_to_objects(komga_search_response['content'])
        self.pageable: bool = komga_search_response['pageable']
        self.total_elements: int = komga_search_response['totalElements']
        self.total_pages: int = komga_search_response['totalPages']
        self.last: bool = komga_search_response['last']
        self.size: int = komga_search_response['size']
        self.number: int = komga_search_response['number']
        self.sort: dict = komga_search_response['sort']
        self.number_of_elements: int = komga_search_response['numberOfElements']
        self.first: bool = komga_search_response['first']
        self.empty: bool = komga_search_response['empty']

