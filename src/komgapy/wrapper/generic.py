import os, json
from komgapy.util import (
    validate_item_type,
    make_endpoint,
    make_param_key,
    remove_duplicates,
    set_search_params,
)
from komgapy.convert_response_util import convert_item_list_to_objects
from komgapy.response_classes import KomgaSeries, KomgaBook, KomgaCollection, KomgaReadlist, KomgaErrorResponse, KomgaSearchResponse
from komgapy.wrapper import RequestAdapter

from PIL import Image
from PIL.PngImagePlugin import PngImageFile
import io
from requests import Response

class Generic(RequestAdapter):

    def _get_item(
            self,
            item_type: str,
            item_id: str = None,
            item_name: str = None
            ) -> KomgaSeries | KomgaBook | KomgaCollection | KomgaReadlist | KomgaErrorResponse | None:
        '''
        Returns Komga object for a single Komga item.
        Can use either id or name of item with id being prefered.
        Using name will search for that name and return first result.

        :param item_type: include series, book(s), collection(s), readlist(s), libraries.
        :param item_id: komga id for item.
        :param item_name: name to search for.
        
        '''

        item_type = validate_item_type(item_type)


        endpoint = make_endpoint(item_type)


        search_params = {'unpaged': True}


        param_key = make_param_key(item_type)

        
        if item_id != None :
            endpoint += '/' + item_id
            search_params[param_key] = item_id 
            name_used = False

        elif endpoint != None:
            search_params['search'] = f'"{item_name}"'
            name_used = True

        else:
            raise Exception('No ID or Name')


        item = self._get_request(endpoint, search_params)


        if type(item) is not list:
            if name_used: item = item.content


        if item == []:
            raise Exception('Search for name returns zero results')

        if type(item) is list:
            for content in item:
                if content.name == item_name:
                    return content


        return item
    

    def _search(self, item_type: str, search_params: dict) -> KomgaSearchResponse | KomgaErrorResponse:
        '''
        Kombga general search
        :param item_type: include series, book(s), collection(s), readlist(s), libraries.
        :param search_params: dictionary of paramiters available for the item. See documentation for options.
        '''

        item_type = validate_item_type(item_type)

        endpoint = make_endpoint(item_type)
        search_list = self._get_request(endpoint, search_params)
    
        return (search_list)
        # return convert_item_list_to_objects(search_list)

    def _update_existing_item(self, item_type, data, item = None, item_id = None, item_name = None, overwrite = False):
        
        if item == None:

            if item_id != None:
                item = self._get_item(item_type, item_id)

            elif item_name != None:
                item = self._get_item(item_type, item_name=item_name)

            else:
                raise Exception('No readlist, id, or name')

        match item_type:
            case 'readlists':
                data_key = 'bookIds'
                current_id_list = item.book_ids
                
            case 'collections':
                data_key = 'seriesIds'
                current_id_list = item.series_ids
                
            case _:
                raise Exception('Incompatible item_type')

        item_id = item.id
        id_list: list = data[data_key]

        if overwrite != True:
            id_list += current_id_list
            data[data_key] = remove_duplicates(id_list)


        if sorted(data[data_key]) != sorted(current_id_list):
            self._overwrite_existing_item(item_type, item_id, data)
            # r = self._patch_request(make_endpoint(item_type, [item_id]), json.dumps(data))
            print('Item Updated')


            item = self._get_item(item_type, item_id)
        else:

            print('Item Doesn\'t Need to be Updated')

        return item
    

    def _overwrite_existing_item(self, item_type, item_id, data):
            r = self._patch_request(make_endpoint(item_type, [item_id]), json.dumps(data))

            return r


    def _update_item_poster(self, item_type: str, item_id: str, file_path: str) -> None | KomgaErrorResponse:
        '''
        Update the poster art for an item from a local file. 
        Tested with collections and readlists.
        '''
        file_name = os.path.basename(file_path)


        endpoint = make_endpoint(item_type, [item_id, 'thumbnails?selected=true'])
        
        headers={'accept':'application/json'}

        files = {'file': (file_name, open(file_path, 'rb'), 'image/png')}

        r = self._post_request(endpoint, files=files, headers=headers)
        if r != None:
            return r
    

    def _item_in_container(self, item_type, container__type, container_id, search_params = None) -> list | KomgaErrorResponse:

           endpoint = make_endpoint(container__type, endpoint_params = [container_id, item_type])
           search_params = set_search_params(search_params, make_param_key(container__type))
           item_list = self._get_request(endpoint, search_params)

           return convert_item_list_to_objects(item_list)
    

    def _add_new_user_generated_item(self,item_type, data):
        return self._post_request(make_endpoint(item_type), json.dumps(data) )
    

    def _update_item_metadata(self, item_type, item_id, data: dict):
        
        data = json.dumps(data)
        endpoint = make_endpoint(item_type, [item_id, 'metadata'])
        r = self._patch_request(endpoint, data, headers={'Content-Type': 'application/json'})
        return r

    def _get_item_poster(self, item_type: str, item_id: str, convert_to_png: bool = True) -> PngImageFile | Response:
        endpoint = make_endpoint(item_type, [item_id, 'thumbnail'])
        r = self._get_request(endpoint, {'id': item_id})
        if convert_to_png and not isinstance(r, KomgaErrorResponse):  
            return Image.open(io.BytesIO(r._content))
        else: 
             return r