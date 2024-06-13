from komgapy.util import make_endpoint  
from komgapy.response_classes import KomgaLibrary, KomgaErrorResponse
from komgapy.wrapper import Generic
import json
from requests import Response


class Library(Generic):

    def get_library(self, library_id = None, library_name = None):
        return self._get_item('libraries', item_id= library_id, item_name= library_name)
    

    def list_all_libraries(self):
        endpoint = make_endpoint('libraries')
        return self._get_request(endpoint, {})
    

    def update_library(self, library_id,  data) -> Response:
        data = json.dumps(data)
        endpoint = make_endpoint('libraries', library_id)
        return self._patch_request(endpoint, data, headers={'Content-Type': 'application/json'})


    def analyze_library(self, library_id) -> Response:
        endpoint = make_endpoint('libraries', [library_id, 'analyze'])
        return self._post_request(endpoint, headers=None, params = {'libraryId': library_id})


    def empty_library_trash(self, library_id) -> Response:
        endpoint = make_endpoint('libraries', [library_id, 'empty-trash'])
        return self._post_request(endpoint, headers=None, params = {'libraryId': library_id})


    def refresh_library_metadata(self, library_id) -> Response:
        endpoint = make_endpoint('libraries', [library_id, 'metadata', 'refresh'])
        return self._post_request(endpoint, headers=None, params = {'libraryId': library_id})


    def scan_library(self, library_id, deep: bool = False) -> Response:
        endpoint = make_endpoint('libraries', [library_id, 'scan'])
        return self._post_request(endpoint, headers=None, params={'libraryId': library_id, 'deep': deep})


