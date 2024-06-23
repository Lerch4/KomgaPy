from komgapy.response_classes import KomgaCollection, KomgaErrorResponse
from komgapy.wrapper import Generic


class Collection(Generic):

    def get_collection(self, collection_id: str = None, collection_name: str = None) -> KomgaCollection | KomgaErrorResponse:
        '''
        Returns a single Komga collection object.
        Takes a collection id or name with id being prefered.
        '''
        return self._get_item('collections', collection_id, collection_name)


    def search_collection(self, search_params: dict):
        '''
        Komga Search

        :param search_params: dictionary of paramiters available for collections. See documentation for options.
        '''        
        return self._search('collections', search_params)
    

    def update_collection_poster(self, collection_id: str, file_path: str):
        '''
        Add poster art to collection and make active
        '''
        return self._update_item_poster('collections', collection_id, file_path)


    def collections_in_series(self, series_id: str, search_params: dict = None) -> list[KomgaCollection] | KomgaErrorResponse:
        '''
        Returns all collections in a series given the series id
        '''
        return self._item_in_container('collections', 'series', series_id, search_params)


    def add_new_collection(self, data: dict):
        '''
        Add new collection from data

        :param data: See docs for keys
        '''
        return self._add_new_user_generated_item('collections', data)
    

    def update_existing_collection(
            self,
            data: dict,
            collection: KomgaCollection = None,
            collection_id: str = None,
            collection_name: str = None,
            overwrite: bool = False
            ):
        '''
        Update existing readlist.
        Takes either collection object, name, or id with collection object being prefered.

        :param data: New data to be added, see docs for keys.
        :param readlist: Komga object to be updated(prefred)
        :param readlist_id: Komga id for collection
        :param readlist_name: Exact name of collection
        :param overwrite: True replaces old data with new data, False appends new data to old data.
        '''  

        return self._update_existing_item('collections', data=data, item = collection, item_id = collection_id, item_name = collection_name, overwrite=overwrite)
    
    def get_collection_poster(self, collection_id: str, convert_to_png: bool = True):
        '''
        Returns collection thumbnail poster as a png image file. 
        Can get raw response by setting convert_to_png = false.
        '''
        return self._get_item_poster('collections', collection_id, convert_to_png)
    