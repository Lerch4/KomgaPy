import json, requests, io

from komgapy.util import make_endpoint
from komgapy.wrapper.request_adapter import RequestAdapter
from komgapy.response_classes import KomgaReadlist, KomgaBook, KomgaErrorResponse, cbl_match_response
from komgapy.wrapper.parent_classes import KomgaItem, Generic, Groups, FileAccess
from komgapy.wrapper.util_methods import item_in_container


class Readlists(KomgaItem, Groups, Generic, FileAccess):
    
    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None:
        self._ra = RequestAdapter(komga_url, auth)


    # From KomgaItem Parent Class
    def get(self, id: str = None, name: str = None) -> KomgaReadlist | KomgaErrorResponse:
        '''
        Returns a single Komga readlist object.
        Takes a readlist id or name with id being prefered.
        '''
        # return self._get_item('readlists', readlist_id, readlist_name)
        return super().get('readlists', id, name)
    

    def search(self, search_params: dict):
        '''
        Komga Search
        :param search_params: dictionary of paramiters available for readlists. See documentation for options.
        '''
        return super().search('readlists', search_params)


    def update_poster(self, readlist_id: str, file_path: str):
        '''
        Add poster art to readlist and make active
        '''
        return super().update_poster('readlists', readlist_id, file_path)    


    def poster(self, readlist_id: str, convert_to_png: bool = True):
        '''
        Returns readlist thumbnail poster as a png image file. 

        :param convert_to_png: True returns a png file, False returns Bytes object 
        '''    
        return super().poster('readlists', readlist_id, convert_to_png)
    

    # From Groups Parent Class
    def overwrite(self, readlist_id: str, data: dict):
        '''
        Replaces current data with new data for readlist
        '''
        return super().overwrite('readlists', readlist_id, data)


    def new(self, data: dict):
        '''
        Add new readlist from data

        :param data: See docs for keys
        '''
        return super().new('readlists', data)


    def remove(self, readlist_id):
        '''
        Removes Readlist (this cannot be undone)
        '''
        return super().remove('readlists', readlist_id)
    

    # Methods for Readlists, Series, Books
    def files(self, readlist_id: str, convert_to_zip: bool = True):
        '''
        Returns readlist files as a zip(cbz) file or Bytes object. 

        :param convert_to_zip: True returns a zip file, False returns Bytes object 
        '''
        return super().files(self, readlist_id, convert_to_zip)


    def save_files(self, readlist_id: str, path: str):
        '''
        Saves the readlist to path

        :param path: path to save location including name and extention
        '''
        super().save_files('readlists', readlist_id, path)


    # Readlist specific methods 
    def books(self, readlist_id: str, search_params: dict = None) -> list[KomgaBook] | KomgaErrorResponse:
        '''
        Returns all books in a readlist given the readlist id
        '''
        return item_in_container('books', 'readlists', readlist_id, search_params)


    def next_book(self, readlist_id, book_id):
        endpoint = make_endpoint('readlists', [readlist_id, 'books', book_id, 'next'])
        return self._ra._get_request(endpoint, {'id': readlist_id, 'bookId': book_id})


    def previous_book(self, readlist_id, book_id):
        endpoint = make_endpoint('readlists', [readlist_id, 'books', book_id, 'previous'])
        return self._ra._get_request(endpoint, {'id': readlist_id, 'bookId': book_id})
    

    def match_cbl(self, cbl: str, input: str ='path', output: str = 'content' ):
        '''
        :param cbl: cbl file from path, url, or raw
        :param input: 'path' (default), 'url', or 'raw'
        :param output: format data to be returned in. content returns match response object. raw returns raw response. 
        '''
        endpoint = '/api/v1/readlists/match/comicrack'
        match input:
            case 'path':
                with open(cbl, 'r') as f:
                    file = {'file': f.read()}
            case 'url':
                r = requests.get(cbl)
                f = io.TextIOWrapper(io.BytesIO(r._content))
                file = {'file': f}
            case 'raw':
                file = {'file': cbl}
            case _:
                raise Exception('Ivalid input: Must be in [path, url, raw]')

        r = self._ra._post_request(endpoint, files=file, headers={'accept': 'application/json'})

        if output == 'content':
            return cbl_match_response(json.loads(r.text))

        else: return r

        

        



    




