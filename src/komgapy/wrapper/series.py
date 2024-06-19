from komgapy.response_classes import*
from komgapy.wrapper import Generic


class Series(Generic):

    def get_series(self, series_id: str = None, series_name: str = None) -> KomgaSeries | KomgaErrorResponse:
        '''
        Returns Komga object for a single Komga item.
        Can use either id or name of item with id being prefered.
        Using name will search for that name and return first result.

        :param series_id: Komga series id
        :param item_name: Exact name to search for.
        
        '''
        return self._get_item('series', series_id, series_name)


    def search_series(self, search_params) -> KomgaSearchResponse | KomgaErrorResponse:
        '''
        Kombga general search.
        :param search_params: dictionary of paramiters available for series. See documentation for options.       
        '''
        return self._search('series', search_params)


    def update_series_poster(self, series_id, file_path):
        '''
        Updates the poster thumbnail for a series given the series id.
        Untested.
        '''
        return self._update_item_poster('series', series_id, file_path)


    def series_in_collection(self, collection_id, search_params = None) -> list[KomgaSeries] | KomgaErrorResponse:
        '''
        Returns all series in a collection given the collection id
        '''
        return self._item_in_container('series', 'collections', collection_id, search_params)


    def update_series_metadata(self, series_id: str, data: dict):
        '''
        Updates metadata for a series.

        :param sereis_id: Komga series id
        :param data: Data to be updated. See docs for keys.
        '''
        return self._update_item_metadata('series', series_id, data)


    def get_series_poster(self, series_id: str, convert_to_png: bool = True):
        '''
        Returns series thumbnail poster as a png image file. 

        :param convert_to_png: Can get raw response by setting convert_to_png = false.
        '''
        return self._get_item_poster('series', series_id, convert_to_png)


    def get_series_file(self, series_id, convert_to_zip: bool = True):
        return self._get_file(series_id, convert_to_zip)

    def save_series_files(self, series_id, path):
        '''
        Saves the series to path

        :param path: path to save location including name and extention
        '''
        self._save_file('series', series_id, path)