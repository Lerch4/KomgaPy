import json

from komgapy.util import make_endpoint  
from komgapy.response_classes import KomgaLibrary
from komgapy.wrapper.request_adapter import RequestAdapter
from komgapy.wrapper.parent_classes import Generic
from requests import Response


class Libraries(Generic):
    
    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None:
        self._ra = RequestAdapter(komga_url, auth)

    def get(self, library_id: str = None, library_name: str = None):
        '''
        Returns a single Komga library object.
        Takes a library id or name with id being prefered.
        '''
        return super().get('libraries', item_id = library_id, item_name = library_name)
    

    def all(self) -> list[KomgaLibrary]:
        '''
        List all libraries on server
        '''
        endpoint = make_endpoint('libraries')
        return self._ra._get_request(endpoint, {})
    

    def update(self, library_id: str,  data: dict) -> Response:
        '''
        Update library from data.

        :param library_id: Komga id from library
        :param data: Data to be updated(see docs for keys)
        '''
        data = json.dumps(data)
        endpoint = make_endpoint('libraries', library_id)
        return self._ra._patch_request(endpoint, data, headers={'Content-Type': 'application/json'})


    def analyze(self, library_id: str) -> Response:
        '''
        Analyze library from library id.
        '''
        endpoint = make_endpoint('libraries', [library_id, 'analyze'])
        return self._ra._post_request(endpoint, headers=None, params = {'libraryId': library_id})


    def empty_trash(self, library_id: str) -> Response:
        '''
        Empty trash for library from library id.
        '''
        endpoint = make_endpoint('libraries', [library_id, 'empty-trash'])
        return self._ra._post_request(endpoint, headers=None, params = {'libraryId': library_id})


    def refresh_metadata(self, library_id: str) -> Response:
        '''
        Refresh metadata for library from library id.
        '''
        endpoint = make_endpoint('libraries', [library_id, 'metadata', 'refresh'])
        return self._ra._post_request(endpoint, headers=None, params = {'libraryId': library_id})


    def scan(self, library_id: str, deep: bool = False) -> Response:
        '''
        Scan library from library id.

        :param deep: True runs deep scan
        '''
        endpoint = make_endpoint('libraries', [library_id, 'scan'])
        return self._ra._post_request(endpoint, headers=None, params={'libraryId': library_id, 'deep': deep})


