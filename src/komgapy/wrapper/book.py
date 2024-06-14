from komgapy.response_classes import KomgaBook, KomgaErrorResponse
from komgapy.wrapper import Generic


class Books(Generic):

    def get_book(self, book_id = None, book_name = None) -> KomgaBook | KomgaErrorResponse | str:
        return self._get_item('books', book_id, book_name)
    

    def search_books(self, search_params):
        return self._search('books', search_params)
    
    
    def update_book_poster(self, book_id, file_path):
        '''
        Untested
        '''
        return self._update_item_poster('book', book_id, file_path)
    

    def update_book_metadata(self, book_id, data: dict):
        return self._update_item_metadata('books', book_id, data)
    
        
    def books_in_series(self, series_id, search_params = None) -> list[KomgaBook] | KomgaErrorResponse:
        '''
        Returns all books in a series given the series id
        '''
        return self._item_in_container('books', 'series', series_id, search_params)


    def books_in_readlist(self, readlist_id, search_params = None) -> list[KomgaBook] | KomgaErrorResponse:
        '''
        Returns all books in a readlist given the readlist id
        '''
        return self._item_in_container('books', 'readlists', readlist_id, search_params)

    def get_book_poster(self, book_id: str, convert_to_png: bool = True):
        '''
        Returns book thumbnail poster as a png image file. 
        Can get raw response by setting convert_to_png = false.
        '''
        return self._get_item_poster('books', book_id, convert_to_png)
