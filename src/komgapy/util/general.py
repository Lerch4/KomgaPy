

def make_endpoint(item_type: str,  endpoint_params: list[str]|str = None, version: str = "v1") -> str:
    '''
    Returns an API endpoint
    :param item_type: The API controller used. Includes books, series, collections, readlists, libraries
    :param endpoint_params: Additional parameters added on to item_type. Multiple endpoint params can be added as a list
    :param version: API version to use in endpoint
    '''

    endpoint = f'/api/{version}/{item_type.lower()}' 

    if endpoint_params!= None:
        endpoint += '/'

        if type(endpoint_params) == list:
            endpoint += '/'.join(endpoint_params)

        elif type(endpoint_params) == str:
            endpoint += endpoint_params
    
    return endpoint


def make_param_key(item_type: str) -> str:
    '''
    Returns the correct type of id parameter key based on the item type
    '''
    if item_type in ['collections', 'readlists']:
        param_key = 'id'
    elif item_type == 'series':
        param_key = f'{item_type}Id'
    else:  
        param_key = f'{item_type[:-1]}Id'
    
    return param_key


def set_search_params(search_params: dict, default):
    '''
    If search parameters doesnt exist set to default.
    '''
    if search_params == None:
        search_params = default
    return search_params


def validate_item_type(item_type: str) -> str:
    '''
    Validates that item type is one of books, series, collections, readlists, libraries
    Will accept book, collection, readlist and make them plural
    '''
    if item_type[-1] != 's': item_type += 's'
    
    if item_type not in ['books', 'series', 'collections', 'readlists', 'libraries']:
       raise Exception('item_type must be one of: books, series, collections, readlists, libraries')

    return item_type


def remove_duplicates(data: list) -> list:
    '''
    Takes a list and returns that list with no duplicates
    '''
    data_no_dups = []
    for item in data:
        if item not in data_no_dups:
            data_no_dups.append(item)
    
    return data_no_dups
