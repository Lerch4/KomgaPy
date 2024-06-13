
import json

from requests import Response

from komgapy.response_classes import  KomgaSeries, KomgaBook, KomgaCollection, KomgaReadlist, KomgaLibrary, KomgaErrorResponse, KomgaSearchResponse
from komgapy.convert_response_util import convert_response_to_komga_item

def make_endpoint(item_type: str,  endpoint_params: list|str = None, version: str = "v1") -> str:

    endpoint = f'/api/{version}/{item_type.lower()}' 


    if endpoint_params!= None:
        endpoint += '/'

        if type(endpoint_params) == list:
            endpoint += '/'.join(endpoint_params)

        elif type(endpoint_params) == str:
            endpoint += endpoint_params
    
    
    return endpoint


def make_param_key(item_type: str):
    if item_type in ['collections', 'readlists']:
        param_key = 'id'
    elif item_type == 'series':
        param_key = f'{item_type}Id'
    else:  
        param_key = f'{item_type[:-1]}Id'
    
    return param_key


def set_search_params(search_params: dict, default):
    if search_params == None:
        search_params = default
    return search_params


def validate_item_type(item_type):
    if item_type[-1] != 's': item_type += 's'
    
    if item_type not in ['books', 'series', 'collections', 'readlists', 'libraries']:
       raise Exception('item_type must be one of: books, series, collections, readlists, libraries')

    return item_type


def remove_duplicates(data: list):
    data_no_dups = []
    for item in data:
        if item not in data_no_dups:
            data_no_dups.append(item)
    
    return data_no_dups

 
def convert_response_to_object(response: Response) -> (
        Response |
        KomgaErrorResponse |
        KomgaSearchResponse |
        KomgaSeries |
        KomgaBook |
        KomgaCollection |
        KomgaReadlist
        ):

    if response.text:

        try: 
            response_json = json.loads(response.text)
            
        except json.decoder.JSONDecodeError:
            return response

        if type(response_json) is list and response_json != []:
            if type(response_json[0]) is dict:
                if 'root' in response_json[0].keys():
                    library_list = []
                    for library in response_json:
                        library_list.append(KomgaLibrary(library))
                    return library_list
            return response_json

        if 'message' in response_json.keys():
            return KomgaErrorResponse(response_json)
        
        elif 'content' in response_json.keys():
            return KomgaSearchResponse(response_json)
        
        elif 'id' in response_json.keys():
            return convert_response_to_komga_item(response_json)
        
 
    return response
