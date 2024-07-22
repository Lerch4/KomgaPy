from komgapy.response_classes import KomgaBook, KomgaErrorResponse
from komgapy.wrapper.request_adapter import RequestAdapter
from komgapy.wrapper.parent_classes import KomgaItem, Generic, Content, FileAccess

from komgapy.util import make_endpoint
from komgapy.wrapper.util_methods import item_in_container


class Books(KomgaItem, Content, Generic, FileAccess):

    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None:
        self._ra = RequestAdapter(komga_url, auth)


    # From KomgaItem Parent Class
    def get(self, id: str = None, name: str = None) -> KomgaBook | KomgaErrorResponse:
        '''
        Returns a single KomgaBook object
        Takes either id or name of item with id being prefered.
        Using name will search for that name and return first result.

        :param readlist_id: Komga id for readlist.
        :param readlist_name: Exact name to search for.
        '''
        return super().get('books', id, name)
    

    def search(self, search_params: dict):
        '''
        Komga general search
        :param search_params: dictionary of paramiters available for readlists. See documentation for options.
        '''
        return super().search('books', search_params)


    def poster(self, book_id: str, convert_to_png: bool = True):
        '''
        Returns book thumbnail poster as a png image file. 
        Can get raw response by setting convert_to_png = false.
        '''
        return super().poster('books', book_id, convert_to_png)
    
    
    def update_poster(self, book_id: str, file_path: str):
        '''
        Untested
        '''
        return super().update_poster('book', book_id, file_path)
    

    # From Content Parent Class
    def update_metadata(self, book_id: str, data: dict):
        '''
        Updates metadata for book
        :param data: see docs for data keys
        '''
        return super().update_metadata('books', book_id, data)
    

    # Methods for Readlists, Series, Books
    def files(self, book_id: str, convert_to_zip: bool = True):
        '''
        Returns the files of the book as zip or as bytes

        :param convert_to_zip: False will return bytes objects and True will return zip file
        '''
        return super().files('books', book_id, convert_to_zip)


    def save_files(self, book_id: str, path: str) -> None:
        '''
        Saves book to path

        :param path: path to save location including name and extention
        '''
        super().save_files('books', book_id, path)



    # Book specific methods 
    def duplicates(self, search_params: dict = None):
        endpoint = make_endpoint('books', 'duplicates')
        return self._ra._get_request(endpoint, search_params)
    
    def ondeck(self, search_params: dict = None):
        endpoint = make_endpoint('books', 'ondeck')
        return self._ra._get_request(endpoint, search_params)
    

    def pages(self, book_id: str, ):
        endpoint = make_endpoint('books', [book_id, 'pages'])
        return self._ra._get_request(endpoint, {'bookId': book_id})
    

    def page(self, book_id: str, page_number: int, search_params = None):
        endpoint = make_endpoint('books', [book_id, 'pages', page_number])
        return self._ra._get_request(endpoint, search_params)
    

    def raw_page(self, book_id: str, page_number: int):
        endpoint = make_endpoint('books', [book_id, 'pages', page_number, 'raw'])
        return self._ra._get_request(endpoint, {'bookId': book_id, 'pageNumber' : page_number})
    

    def positions(self, book_id):
        endpoint = make_endpoint('books', [book_id, 'positions'])
        return self._ra._get_request(endpoint, {'bookId': book_id})


    def next_book(self, book_id):
        endpoint = make_endpoint('books', [book_id, 'next'])
        return self._ra._get_request(endpoint, {'bookId': book_id})
    

    def previous_book(self, book_id):
        endpoint = make_endpoint('books', [book_id, 'previous'])
        return self._ra._get_request(endpoint, {'bookId': book_id})
    
    def manifest(self, book_id, file_type = None):
        endpoint = make_endpoint('books', [book_id, 'manifest', file_type])
        return self._ra._get_request(endpoint, {'bookId': book_id})
    
    
    def readlists(self, book_id: str, search_params: dict = None):
        '''
        Returns all readlists that a book is in given the book id.

        :param search_params: additional parameters to narrow down results(see docs for keys)
        '''
        return item_in_container('readlists', 'books', book_id, search_params )


