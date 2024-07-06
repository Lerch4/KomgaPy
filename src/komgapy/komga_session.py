from komgapy.wrapper import Series, Books, Collection, Readlist, Library, Referential
from komgapy.util import make_endpoint, make_param_key


class KomgaSession(Series, Books, Collection, Readlist, Library, Referential):
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

    # def make_readlist_from_cbl(self, file: str):
    #     endpoint = '/api/v1/readlists/match/comicrack'
    #     # test = open(path)
    #     data = {'file': file}
    #     print(data)
    #     r = self._post_request(endpoint, data=data, headers={'accept': 'application/json'})
    #     return r



    # def get_posters_in_collection(self, id) : # list[KomgaThumbnail]
    #     '''
    #     Untested
    #     '''
    #     return self._item_in_container('thumbnails', 'collections', id)

    
