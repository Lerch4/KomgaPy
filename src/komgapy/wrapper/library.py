from komgapy.util import make_endpoint  
from komgapy.response_classes import KomgaLibrary, KomgaErrorResponse
from komgapy.wrapper import Generic
import json
from requests import Response


class Library(Generic):

    def get_library(self, library_id: str = None, library_name: str = None):
        '''
        Returns a single Komga library object.
        Takes a library id or name with id being prefered.
        '''
        return self._get_item('libraries', item_id = library_id, item_name = library_name)
    

    def list_all_libraries(self) -> list[KomgaLibrary]:
        '''
        List all libraries on server
        '''
        endpoint = make_endpoint('libraries')
        return self._get_request(endpoint, {})
    

    def update_library(self, library_id: str,  data: dict) -> Response:
        '''
        Update library from data.

        :param library_id: Komga id from library
        :param data: Data to be updated(see docs for keys)
        '''
        data = json.dumps(data)
        endpoint = make_endpoint('libraries', library_id)
        return self._patch_request(endpoint, data, headers={'Content-Type': 'application/json'})


    def analyze_library(self, library_id: str) -> Response:
        '''
        Analyze library from library id.
        '''
        endpoint = make_endpoint('libraries', [library_id, 'analyze'])
        return self._post_request(endpoint, headers=None, params = {'libraryId': library_id})


    def empty_library_trash(self, library_id: str) -> Response:
        '''
        Empty trash for library from library id.
        '''
        endpoint = make_endpoint('libraries', [library_id, 'empty-trash'])
        return self._post_request(endpoint, headers=None, params = {'libraryId': library_id})


    def refresh_library_metadata(self, library_id: str) -> Response:
        '''
        Refresh metadata for library from library id.
        '''
        endpoint = make_endpoint('libraries', [library_id, 'metadata', 'refresh'])
        return self._post_request(endpoint, headers=None, params = {'libraryId': library_id})


    def scan_library(self, library_id: str, deep: bool = False) -> Response:
        '''
        Scan library from library id.

        :param deep: True runs deep scan
        '''
        endpoint = make_endpoint('libraries', [library_id, 'scan'])
        return self._post_request(endpoint, headers=None, params={'libraryId': library_id, 'deep': deep})


