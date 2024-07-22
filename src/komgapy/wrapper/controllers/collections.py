from komgapy.wrapper.request_adapter import RequestAdapter
from komgapy.response_classes import KomgaCollection, KomgaSeries, KomgaErrorResponse
from komgapy.wrapper.parent_classes import KomgaItem, Groups, Generic
from komgapy.wrapper.parent_classes.groups import Groups
from komgapy.wrapper.util_methods import item_in_container


class Collections(KomgaItem, Groups, Generic):
    
    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None:
        self._ra = RequestAdapter(komga_url, auth)


    # From KomgaItem Parent Class
    def get(self, id: str = None, name: str = None) -> KomgaCollection | KomgaErrorResponse:
        '''
        Returns a single Komga collection object.
        Takes a collection id or name with id being prefered.
        '''
        return super().get('collections', id, name)
 

    def search(self, search_params: dict):
        '''
        Komga Search

        :param search_params: dictionary of paramiters available for collections. See documentation for options.
        '''        
        return super().search('collections', search_params)
    

    def poster(self, collection_id: str, convert_to_png: bool = True):
        '''
        Returns collection thumbnail poster as a png image file. 
        Can get raw response by setting convert_to_png = false.
        '''
        return super().poster('collections', collection_id, convert_to_png)


    def update_poster(self, collection_id: str, file_path: str):
        '''
        Add poster art to collection and make active
        '''
        return super().update_poster('collections', collection_id, file_path)


    # From Groups Parent Class
    def overwrite(self, readlist_id: str, data: dict):
            '''
            Replaces current data with new data for collecrtion
            '''
            return super().overwrite('collections', readlist_id, data)


    def new(self, data: dict):
        '''
        Add new collection from data

        :param data: See docs for keys
        '''
        return super().new('collections', data)
    
    
    def remove(self, collection_id):
        '''
        Removes from library (this cannot be undone)
        '''
        return super().remove('collections', collection_id)
    

   # Collection specific methods 
    def series(
            self,
            collection_id: str,
            search_params: dict = None
            ) -> list[KomgaSeries] | KomgaErrorResponse:
        '''
        Returns all series in a collection given the collection id
        '''
        return item_in_container('series', 'collections', collection_id, search_params)


