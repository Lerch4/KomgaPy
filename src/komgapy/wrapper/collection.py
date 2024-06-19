from komgapy.response_classes import KomgaCollection, KomgaErrorResponse
from komgapy.wrapper import Generic


class Collection(Generic):

    def get_collection(self, collection_id = None, collection_name = None) -> KomgaCollection | KomgaErrorResponse | str:
        return self._get_item('collections', collection_id, collection_name)


    def search_collection(self, search_params):
        return self._search('collections', search_params)
    

    def update_collection_poster(self, collection_id, file_path):
        '''
        Add poster art to collection and make active
        '''
        return self._update_item_poster('collections', collection_id, file_path)


    def collections_in_series(self, series_id, search_params = None) -> list[KomgaCollection] | KomgaErrorResponse:
        '''
        Returns all collections in a series given the series id
        '''
        return self._item_in_container('collections', 'series', series_id, search_params)


    def add_new_collection(self, data):
        return self._add_new_user_generated_item('collections', data)
    

    def update_existing_collection(self, data, collection = None, collection_id=None, collection_name = None, overwrite = False):
        return self._update_existing_item('collections', data=data, item = collection, item_id = collection_id, item_name = collection_name, overwrite=overwrite)
    
    def get_collection_poster(self, collection_id: str, convert_to_png: bool = True):
        '''
        Returns collection thumbnail poster as a png image file. 
        Can get raw response by setting convert_to_png = false.
        '''
        return self._get_item_poster('collections', collection_id, convert_to_png)
    