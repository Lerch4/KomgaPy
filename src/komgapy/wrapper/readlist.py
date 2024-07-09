import json
from io import TextIOWrapper
from komgapy.response_classes import KomgaReadlist, KomgaErrorResponse, cbl_match_response
from komgapy.wrapper import Generic


class Readlist(Generic):

    def get_readlist(self, readlist_id: str = None, readlist_name: str = None) -> KomgaReadlist | KomgaErrorResponse:
        '''
        Returns a single Komga readlist object.
        Takes a readlist id or name with id being prefered.
        '''
        return self._get_item('readlists', readlist_id, readlist_name)
    

    def search_readlists(self, search_params: dict):
        '''
        Komga Search
        :param search_params: dictionary of paramiters available for readlists. See documentation for options.
        '''
        return self._search('readlists', search_params)


    def update_readlist_poster(self, readlist_id: str, file_path: str):
        '''
        Add poster art to readlist and make active
        '''
        return self._update_item_poster('readlists', readlist_id, file_path)    

    
    def add_new_readlist(self, data: dict):
        '''
        Add new readlist from data

        :param data: See docs for keys
        '''
        return self._add_new_user_generated_item('readlists', data)
    

    def update_existing_readlist(
            self,
            data: dict,
            readlist: KomgaReadlist = None,
            readlist_id: str = None,
            readlist_name: str = None,
            overwrite: bool = False
            ):
        '''
        Update existing readlist.
        Takes either readlist object, name, or id with readlist object being prefered.

        :param data: New data to be added, see docs for keys.
        :param readlist: Komga object to be updated(prefred)
        :param readlist_id: Komga id for readlist
        :param readlist_name: Exact name of realist
        :param overwrite: True replaces old data with new data, False appends new data to old data.
        '''
        return self._update_existing_item(
            'readlists',
            data = data,
            item = readlist,
            item_id = readlist_id,
            item_name = readlist_name,
            overwrite = overwrite
            )
    

    def readlist_in_books(self, book_id: str, search_params: dict = None):
        '''
        Returns all readlists that a book is in given the book id.

        :param search_params: additional parameters to narrow down results(see docs for keys)
        '''
        return self._item_in_container('readlists', 'books', book_id, search_params )


    def get_readlist_poster(self, readlist_id: str, convert_to_png: bool = True):
        '''
        Returns readlist thumbnail poster as a png image file. 

        :param convert_to_png: True returns a png file, False returns Bytes object 
        '''    
        return self._get_item_poster('readlists', readlist_id, convert_to_png)
    

    def get_readlist_files(self, readlist_id: str, convert_to_zip: bool = True):
        '''
        Returns readlist files as a zip(cbz) file or Bytes object. 

        :param convert_to_zip: True returns a zip file, False returns Bytes object 
        '''
        return self._get_file(self, readlist_id, convert_to_zip)


    def save_readlist_files(self, readlist_id: str, path: str):
        '''
        Saves the readlist to path

        :param path: path to save location including name and extention
        '''
        self._save_file('readlists', readlist_id, path)


    def match_readlist_cbl(self, file: TextIOWrapper, format: str = 'content'):
        '''
        :param file: file object as TextIOWrapper
        :param format: format data to be returned in. content returns match response object. raw returns raw response. 
        '''
        endpoint = '/api/v1/readlists/match/comicrack'
        file = {'file': file}
        r = self._post_request(endpoint, files=file, headers={'accept': 'application/json'})

        if format == 'content':
            return cbl_match_response(json.loads(vars(r)['_content']))
        else: return r
    
    def match_readlist_cbl_from_path(self, file_path: str, format: str = 'content'):
        '''
        :param file_path: file path of cbl file
        :param format: format data to be returned in. content returns match response object. raw returns raw response. 
        '''
        endpoint = '/api/v1/readlists/match/comicrack'
        with open(file_path, 'r') as f:
            file = {'file': f}
            r = self._post_request(endpoint, files=file, headers={'accept': 'application/json'})

        if format == 'content':
            return cbl_match_response(json.loads(vars(r)['_content']))
        else: return r