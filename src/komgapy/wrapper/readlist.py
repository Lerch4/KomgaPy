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


