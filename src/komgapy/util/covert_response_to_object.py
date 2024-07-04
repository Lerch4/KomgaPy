import json
from requests import Response
from komgapy.util.convert_data_to_komga_object import convert_response_to_komga_object
from komgapy.response_classes import (
    KomgaErrorResponse,
    KomgaSearchResponse,
    KomgaSeries,
    KomgaBook,
    KomgaCollection,
    KomgaReadlist,
    KomgaLibrary
)


def convert_response_to_object(response: Response) -> (
        Response |
        KomgaErrorResponse |
        KomgaSearchResponse |
        KomgaSeries |
        KomgaBook |
        KomgaCollection |
        KomgaReadlist |
        KomgaLibrary | 
        list[KomgaLibrary]
        ):
    '''
    Converts an api Response object to Komga object
    '''

    if response.text:

        try: 
            response_json = json.loads(response.text)
            
        except json.decoder.JSONDecodeError:
            return response

        if type(response_json) is list:
            if response_json != [] and type(response_json[0]) is dict:
                if 'root' in response_json[0]:
                    library_list = []
                    for library in response_json:
                        library_list.append(KomgaLibrary(library))
                    return library_list
            return response_json

        elif 'message' in response_json:
            return KomgaErrorResponse(response_json)
        
        elif 'content' in response_json:
            return KomgaSearchResponse(response_json)
        
        elif 'id' in response_json:
            return convert_response_to_komga_object(response_json)
        
 
    return response