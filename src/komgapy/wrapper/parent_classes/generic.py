from komgapy.exception_classes import NoSearchResults
from komgapy.wrapper.request_adapter import RequestAdapter
from komgapy.util import (
    validate_item_type,
    make_endpoint,
    make_param_key
    )
from komgapy.response_classes import (
    KomgaSeries,
    KomgaBook,
    KomgaCollection,
    KomgaReadlist,
    KomgaErrorResponse,
    KomgaLibrary
    )

class Generic():
    '''
    Generic Parent Class for Collections, Readlists, Books, Series, and Libraries
    '''

    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None:
        self._ra = RequestAdapter(komga_url, auth)

    def get(
            session,
            item_type: str,
            id: str| None = None,
            name: str| None = None
            ) -> (
                KomgaSeries |
                KomgaBook |
                KomgaCollection |
                KomgaReadlist |
                KomgaErrorResponse |
                KomgaLibrary | 
                None
                ):
        '''
        Returns Komga object for a single Komga item.
        Takes either id or name of item with id being prefered.
        Using name will search for that name and return first result.

        :param item_type: Include series, book(s), collection(s), readlist(s), libraries.
        :param item_id: Komga id for item.
        :param item_name: Exact name to search for.
        
        '''

        item_type = validate_item_type(item_type)


        endpoint = make_endpoint(item_type)


        search_params = {'unpaged': True}


        param_key = make_param_key(item_type)

        
        if id != None :
            # endpoint = os.path.join(endpoint, item_id)
            endpoint += '/' + id
            search_params[param_key] = id 
            name_used = False

        elif name != None:
            search_params['search'] = f'"{name}"'
            name_used = True

        else:
            raise Exception('No ID or Name')


        item = session._ra._get_request(endpoint, search_params)


        if type(item) is not list:
            if name_used: item = item.content


        if item == []:
            raise NoSearchResults('Search for name returns zero results')

        if type(item) is list:
            for content in item:
                if content.name == name:
                    return content


        return item
