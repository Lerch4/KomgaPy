import io, zipfile

from komgapy.exception_classes import NoSearchResults
from komgapy.util.convert_list_to_komga_objects import convert_item_list_to_objects
from komgapy.util import (
    make_endpoint,
    make_param_key,
    set_search_params,
    validate_item_type
    )
from komgapy.response_classes import (
    KomgaSeries,
    KomgaBook,
    KomgaCollection,
    KomgaReadlist,
    KomgaErrorResponse,
    KomgaLibrary
    )


def item_in_container(
        session,
        item_type: str,
        container__type: str,
        container_id: str,
        search_params: dict = None
        ) -> list | KomgaErrorResponse:
        '''
        Returns a item from another api controller

        :param search_params: different for each item, see docs for more info
        '''

        endpoint = make_endpoint(container__type, endpoint_params = [container_id, item_type])
        search_params = set_search_params(search_params, make_param_key(container__type))
        item_list = session._ra._get_request(endpoint, search_params)

        return convert_item_list_to_objects(item_list)


def get_item(
        session,
        item_type: str,
        item_id: str| None = None,
        item_name: str| None = None
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

    
    if item_id != None :
        # endpoint = os.path.join(endpoint, item_id)
        endpoint += '/' + item_id
        search_params[param_key] = item_id 
        name_used = False

    elif item_name != None:
        search_params['search'] = f'"{item_name}"'
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
            if content.name == item_name:
                return content


    return item
