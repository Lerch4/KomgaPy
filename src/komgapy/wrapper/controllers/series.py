from komgapy.response_classes import KomgaSeries, KomgaErrorResponse, KomgaBook, KomgaCollection
from komgapy.wrapper.request_adapter import RequestAdapter
from komgapy.wrapper.parent_classes import KomgaItem, Generic, Content, FileAccess

from komgapy.wrapper.util_methods import item_in_container


class Series(KomgaItem, Content, FileAccess, Generic):
    
    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None:
        self._ra = RequestAdapter(komga_url, auth)


    # From KomgaItem Parent Class
    def get(self, id: str = None, name: str = None) -> KomgaSeries | KomgaErrorResponse:
        '''
        Returns Komga Series Object for a single Series.
        Can use either id or name  with id being prefered.
        Using name will search for that name and return first result.

        :param series_id: Komga series id
        :param series_name: Exact name to search for.
        
        '''
        return super().get('series', id, name)


    def search(self, search_params: dict):
        '''
        Komga general search.
        :param search_params: dictionary of paramiters available for series. See documentation for options.       
        '''
        return super().search('series', search_params)


    def poster(self, series_id: str, convert_to_png: bool = True):
        '''
        Returns series thumbnail poster as a png image file. 

        :param convert_to_png: Can get raw response by setting convert_to_png = false.
        '''
        return super().poster('series', series_id, convert_to_png)


    def update_poster(self, series_id: str, file_path: str):
        '''
        Updates the poster thumbnail for a series given the series id.
        Untested.
        '''
        return super().update_poster('series', series_id, file_path)


    # From Content Parent Class
    def update_metadata(self, series_id: str, data: dict):
        '''
        Updates metadata for a series.

        :param sereis_id: Komga series id
        :param data: Data to be updated. See docs for keys.
        '''
        return super().update_metadata('series', series_id, data)


    # From FileAccess
    def files(self, series_id: str, convert_to_zip: bool = True):
        '''
        Returns series files as a zip file or Bytes object. 

        :param convert_to_zip: True returns a zip file, False returns Bytes object 
        '''
        return super().files(series_id, convert_to_zip)


    def save_files(self, series_id: str, path: str):
        '''
        Saves the series to path

        :param path: path to save location including name and extention
        '''
        super().save_files('series', series_id, path)


    # Series specific methods 
    def books(self, series_id: str, search_params: dict = None) -> list[KomgaBook] | KomgaErrorResponse:
        '''
        Returns all books in a series given the series id
        '''
        return item_in_container('books', 'series', series_id, search_params)


    def collections(self, series_id: str, search_params: dict = None) -> list[KomgaCollection] | KomgaErrorResponse:
        '''
        Returns all collections in a series given the series id
        '''
        return item_in_container('collections', 'series', series_id, search_params)
        

