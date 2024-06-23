from komgapy.response_classes import*
from komgapy.wrapper import Generic


class Series(Generic):

    def get_series(self, series_id: str = None, series_name: str = None) -> KomgaSeries | KomgaErrorResponse:
        '''
        Returns Komga Series Object for a single Series.
        Can use either id or name  with id being prefered.
        Using name will search for that name and return first result.

        :param series_id: Komga series id
        :param series_name: Exact name to search for.
        
        '''
        return self._get_item('series', series_id, series_name)


    def search_series(self, search_params: dict) -> KomgaSearchResponse | KomgaErrorResponse:
        '''
        Komga general search.
        :param search_params: dictionary of paramiters available for series. See documentation for options.       
        '''
        return self._search('series', search_params)


    def update_series_poster(self, series_id: str, file_path: str):
        '''
        Updates the poster thumbnail for a series given the series id.
        Untested.
        '''
        return self._update_item_poster('series', series_id, file_path)


    def series_in_collection(
            self,
            collection_id: str,
            search_params: dict = None
            ) -> list[KomgaSeries] | KomgaErrorResponse:
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


    def get_series_files(self, series_id: str, convert_to_zip: bool = True):
        '''
        Returns series files as a zip file or Bytes object. 

        :param convert_to_zip: True returns a zip file, False returns Bytes object 
        '''
        return self._get_file(series_id, convert_to_zip)

    def save_series_files(self, series_id: str, path: str):
        '''
        Saves the series to path

        :param path: path to save location including name and extention
        '''
        self._save_file('series', series_id, path)