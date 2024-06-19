from komgapy.response_classes import KomgaReadlist, KomgaErrorResponse
from komgapy.wrapper import Generic


class Readlist(Generic):

    def get_readlist(self, readlist_id = None, readlist_name = None) -> KomgaReadlist | KomgaErrorResponse:
        return self._get_item('readlists', readlist_id, readlist_name)
    

    def search_readlists(self, search_params):
        return self._search('readlists', search_params)


    def update_readlist_poster(self, readlist_id, file_path):
        '''
        Add poster art to readlist and make active
        '''
        return self._update_item_poster('readlists', readlist_id, file_path)    

    
    def add_new_readlist(self, data):
        return self._add_new_user_generated_item('readlists', data)
    

    def update_existing_readlist(self, data, readlist = None, readlist_id=None, readlist_name = None, overwrite = False):
        return self._update_existing_item('readlists', data=data, item = readlist, item_id = readlist_id, item_name = readlist_name, overwrite=overwrite)
    

    def readlist_in_books(self, book_id, search_params=None):
        return self._item_in_container('readlists', 'books', book_id, search_params )


    def get_readlist_poster(self, readlist_id: str, convert_to_png: bool = True):
        '''
        Returns readlist thumbnail poster as a png image file. 
        Can get raw response by setting convert_to_png = false.
        '''    
        return self._get_item_poster('readlists', readlist_id, convert_to_png)
    

    def get_readlist_files(self, readlist_id, convert_to_zip: bool = True):
        return self._get_file(self, readlist_id, convert_to_zip)


    def save_readlist_files(self, readlist_id, path):
        '''
        Saves the readlist to path

        :param path: path to save location including name and extention
        '''
        self._save_file('readlists', readlist_id, path)