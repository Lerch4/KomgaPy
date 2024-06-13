from komgapy.wrapper import Series, Books, Collection, Readlist, Library
from komgapy.util import make_endpoint
from PIL import Image
from PIL.PngImagePlugin import PngImageFile
import io
from requests import Response

class KomgaSession(Series, Books, Collection, Readlist, Library):
    '''
    Wrapper session class for Komga API requests.

    :param komga_url: host url for komga server
    :param auth: username and password
    '''
    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None: 

        self.host_url = komga_url
        self.auth = auth


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # work in progress

    # def make_readlist_from_cbl(self, path):
    #     endpoint = '/api/v1/readlists/match/comicrack'
    #     data = {'file': path}
    #     r = self._post_request(endpoint, data=data, headers={'accept': 'application/json'})
    #     return r


    def get_collection_poster(self, id: str, convert_reponse_to_png: bool = True) -> PngImageFile | Response:
        endpoint = make_endpoint('collections', [id, 'thumbnail'])
        r = self._get_request(endpoint, {'id': id})
        if convert_reponse_to_png:  
            return Image.open(io.BytesIO(r._content))
        else: 
             return r

    # def get_posters_in_collection(self, id) : # list[KomgaThumbnail]
    #     '''
    #     Untested
    #     '''
    #     return self._item_in_container('thumbnails', 'collections', id)


    def list_referential(self, reference, second_reference = None, search_params = None):

            endpoint = make_endpoint(reference, second_reference)
            return self._get_request(endpoint, search_params)

