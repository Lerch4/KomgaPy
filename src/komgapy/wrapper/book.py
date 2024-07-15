from komgapy.response_classes import KomgaBook, KomgaErrorResponse
from komgapy.wrapper import Generic
from komgapy.util import make_endpoint


class Books(Generic):

    def get_book(self, book_id: str = None, book_name: str = None) -> KomgaBook | KomgaErrorResponse:
        '''
        Returns a single KomgaBook object
        Takes either id or name of item with id being prefered.
        Using name will search for that name and return first result.

        :param readlist_id: Komga id for readlist.
        :param readlist_name: Exact name to search for.
        '''
        return self._get_item('books', book_id, book_name)
    

    def search_books(self, search_params: dict):
        '''
        Komga general search
        :param search_params: dictionary of paramiters available for readlists. See documentation for options.
        '''
        return self._search('books', search_params)
    
    
    def update_book_poster(self, book_id: str, file_path: str):
        '''
        Untested
        '''
        return self._update_item_poster('book', book_id, file_path)
    

    def update_book_metadata(self, book_id: str, data: dict):
        '''
        Updates metadata for book
        :param data: see docs for data keys
        '''
        return self._update_item_metadata('books', book_id, data)
    
        
    def books_in_series(self, series_id: str, search_params: dict = None) -> list[KomgaBook] | KomgaErrorResponse:
        '''
        Returns all books in a series given the series id
        '''
        return self._item_in_container('books', 'series', series_id, search_params)


    def books_in_readlist(self, readlist_id: str, search_params: dict = None) -> list[KomgaBook] | KomgaErrorResponse:
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
    
    
    def get_book_files(self, book_id: str, convert_to_zip: bool = True):
        '''
        Returns the files of the book as zip or as bytes

        :param convert_to_zip: False will return bytes objects and True will return zip file
        '''
        return self._get_file('books', book_id, convert_to_zip)


    def save_book_file(self, book_id: str, path: str) -> None:
        '''
        Saves book to path

        :param path: path to save location including name and extention
        '''
        self._save_file('books', book_id, path)


    def book_duplicates(self, search_params: dict = None):
        endpoint = make_endpoint('books', 'duplicates')
        return self._get_request(endpoint, search_params)
    

    def book_ondeck(self, search_params: dict = None):
        endpoint = make_endpoint('books', 'ondeck')
        return self._get_request(endpoint, search_params)
    

    def book_pages(self, book_id: str, ):
        endpoint = make_endpoint('books', [book_id, 'pages'])
        return self._get_request(endpoint, {'bookId': book_id})
    

    def book_page_number(self, book_id: str, page_number: int, search_params = None):
        endpoint = make_endpoint('books', [book_id, 'pages', page_number])
        return self._get_request(endpoint, search_params)
    

    def book_raw_page(self, book_id: str, page_number: int):
        endpoint = make_endpoint('books', [book_id, 'pages', page_number, 'raw'])
        return self._get_request(endpoint, {'bookId': book_id, 'pageNumber' : page_number})
    

    def book_positions(self, book_id):
        endpoint = make_endpoint('books', [book_id, 'positions'])
        return self._get_request(endpoint, {'bookId': book_id})


    def next_book(self, book_id):
        endpoint = make_endpoint('books', [book_id, 'next'])
        return self._get_request(endpoint, {'bookId': book_id})
    

    def previous_book(self, book_id):
        endpoint = make_endpoint('books', [book_id, 'previous'])
        return self._get_request(endpoint, {'bookId': book_id})
    
    def book_manifest(self, book_id, file_type = None):
        endpoint = make_endpoint('books', [book_id, 'manifest', file_type])
        return self._get_request(endpoint, {'bookId': book_id})