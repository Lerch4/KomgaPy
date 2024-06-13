from komgapy.response_classes import*
from komgapy.wrapper import Generic


class Series(Generic):

    def get_series(self, series_id = None, series_name = None) -> KomgaSeries | KomgaErrorResponse:
        return self._get_item('series', series_id, series_name)


    def search_series(self, search_params):
        return self._search('series', search_params)


    def update_series_poster(self, series_id, file_path):
        '''
        Untested
        '''
        return self._update_item_poster('series', series_id, file_path)


    def series_in_collection(self, collection_id, search_params = None) -> list[KomgaSeries] | KomgaErrorResponse:
        '''
        Returns all series in a collection given the collection id
        '''
        return self._item_in_container('series', 'collections', collection_id, search_params)


    def update_series_metadata(self, series_id, data: dict):
        return self._update_item_metadata('series', series_id, data)



