import json
from requests import Response, request
from komgapy.util import convert_response_to_object
from komgapy.response_classes import (
    KomgaErrorResponse,
    KomgaSearchResponse,
    KomgaSeries,
    KomgaBook,
    KomgaCollection,
    KomgaReadlist,
    KomgaLibrary
)


class RequestAdapter:
    '''
    Handles GET, POST, PATCH requests and converts output.
    Parent class to generic class and therfore all wrapper classes.
    '''
    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None: 
        self.host_url = komga_url
        self.auth = auth


    def _generic_request(
            self,
            http_method: str,
            endpoint: str,
            params: dict = None,
            data: dict = None,
            files = None,
            headers: dict = None
            ) -> (
                Response |
                KomgaErrorResponse |
                KomgaSearchResponse |
                KomgaSeries |
                KomgaBook |
                KomgaCollection |
                KomgaReadlist |
                KomgaLibrary
                ):
        '''
        Gets a response from an api request and returns object.
        '''

        full_url = self.host_url + endpoint
        r = request(method=http_method, url=full_url, params=params, data=data, files=files, headers=headers, auth=self.auth)

        return convert_response_to_object(r)


    def _get_request(
            self,
            endpoint: str,
            search_params: dict,
            headers = None
            ):
        '''
        GET Komga api request
        '''

        return (self._generic_request(http_method='GET', endpoint = endpoint, params=search_params, headers=headers))


    def _post_request(
            self,
            endpoint: str,
            data: dict = None,
            files = None,
            params = None,
            headers: dict = {'Content-Type':'application/json', 'accept':'application/json'}
            ):
        '''
        POST Komga api request
        '''
        return (self._generic_request(http_method='POST', endpoint = endpoint, data=data, files=files, headers = headers, params=params))


    def _patch_request(
            self,
            endpoint: str,
            data: dict,
            headers: dict = {'Content-Type':'application/json', 'accept':'application/json'}
            ) -> Response:
        '''
        PATCH Komga api request
        '''
        return self._generic_request(http_method='PATCH', endpoint = endpoint, data=data, headers = headers)

