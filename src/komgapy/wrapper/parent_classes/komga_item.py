import os, io

from PIL import Image
from PIL.PngImagePlugin import PngImageFile

from komgapy.wrapper.request_adapter import RequestAdapter
from komgapy.util import (
    validate_item_type,
    make_endpoint,
    )
from komgapy.response_classes import (
    KomgaErrorResponse,
    KomgaSearchResponse,
    )


class KomgaItem:
    '''
    Parent Class for Collections, Readlists, Books, and Series
    '''

    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None:
        self._ra = RequestAdapter(komga_url, auth)

    def search(
            self,
            item_type: str,
            search_params: dict
            ) -> KomgaSearchResponse | KomgaErrorResponse:
        '''
        Komga general search
        :param item_type: include series, book(s), collection(s), readlist(s), libraries.
        :param search_params: dictionary of paramiters available for the item. See documentation for options.
        '''

        item_type = validate_item_type(item_type)

        endpoint = make_endpoint(item_type)
        search_list = self._ra._get_request(endpoint, search_params)
    
        return (search_list)
        # return convert_item_list_to_objects(search_list)


    def update_poster(
            self,
            item_type: str,
            item_id: str,
            file_path: str
            ) -> None | KomgaErrorResponse:
        '''
        Update the poster art for an item from a local file. 
        Tested with collections and readlists.
        '''
        file_name = os.path.basename(file_path)


        endpoint = make_endpoint(item_type, [item_id, 'thumbnails?selected=true'])
        
        headers={'accept':'application/json'}

        files = {'file': (file_name, open(file_path, 'rb'), 'image/png')}

        r = self._ra._post_request(endpoint, files=files, headers=headers)
        if r != None:
            return r
    

    def poster(self, item_type: str, item_id: str, convert_to_png: bool = True) -> PngImageFile | io.BytesIO | KomgaErrorResponse:
        '''
        Returns png image for an item thumbnail

        :param convert_to_png: False returns raw bytes
        '''
        endpoint = make_endpoint(item_type, [item_id, 'thumbnail'])
        r = self._ra._get_request(endpoint, {'id': item_id}, headers={'accept': 'image/jpeg'})


        if  isinstance(r, KomgaErrorResponse):
            return r
        elif convert_to_png:  
            return Image.open(io.BytesIO(r._content))
        else: 
             return io.BytesIO(r._content)


    # def thumbnails(self, item_type, item_id):
    #     endpoint = make_endpoint(item_type, [item_id, 'thumbnails'])
    #     return self._ra._get_request(endpoint, {make_param_key(item_type): item_id})


