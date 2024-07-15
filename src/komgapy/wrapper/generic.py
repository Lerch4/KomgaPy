import os, json, io, zipfile

from PIL import Image
from PIL.PngImagePlugin import PngImageFile

from komgapy.exception_classes import NoSearchResults
from komgapy.util import (
    validate_item_type,
    make_endpoint,
    make_param_key,
    remove_duplicates,
    set_search_params,
)
from komgapy.wrapper import RequestAdapter
from komgapy.util.convert_list_to_komga_objects import convert_item_list_to_objects
from komgapy.response_classes import (
    KomgaSeries,
    KomgaBook,
    KomgaCollection,
    KomgaReadlist,
    KomgaErrorResponse,
    KomgaSearchResponse,
    KomgaLibrary
    )


class Generic(RequestAdapter):
    '''
    Generic Parent Class
    '''

    def _get_item(
            self,
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
            endpoint += '/' + item_id
            search_params[param_key] = item_id 
            name_used = False

        elif item_name != None:
            search_params['search'] = f'"{item_name}"'
            name_used = True

        else:
            raise Exception('No ID or Name')


        item = self._get_request(endpoint, search_params)


        if type(item) is not list:
            if name_used: item = item.content


        if item == []:
            raise NoSearchResults('Search for name returns zero results')

        if type(item) is list:
            for content in item:
                if content.name == item_name:
                    return content


        return item
    

    def _search(
            self,
            item_type: str,
            search_params: dict
            ) -> KomgaSearchResponse | KomgaErrorResponse:
        '''
        Komga general search
        :param item_type: include series, book(s), collection(s), readlist(s), libraries.
        :param search_params: dictionary of paramiters available for the item. See documentation for options.
        '''

        item_type = validate_item_type(item_type)

        endpoint = make_endpoint(item_type)
        search_list = self._get_request(endpoint, search_params)
    
        return (search_list)
        # return convert_item_list_to_objects(search_list)


    def _update_existing_item(
            self,
            item_type: str,
            data: dict,
            item = None,
            item_id: str = None,
            item_name: str = None,
            overwrite: bool = False
            ):
        '''
        Update existing readlist or collection.
        Takes either item object, name, or id with object being prefered.

        :param item_type: Includes readlists or collections.
        :param data: New data to be added, see docs for keys.
        :param item: Komga object to be updated(prefred)
        :param item_id: Komga id for item
        :param item_name: Exact name of item
        :param overwrite: True replaces old data with new data, False appends new data to old data.


        ''' 
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
    

    def _overwrite_existing_item(self, item_type: str, item_id: str, data: dict):
            '''
            Replaces current data with new data for collections or readlists
            '''
            r = self._patch_request(make_endpoint(item_type, [item_id]), json.dumps(data))

            return r


    def _update_item_poster(
            self,
            item_type: str,
            item_id: str,
            file_path: str
            ) -> None | KomgaErrorResponse:
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
    

    def _item_in_container(
            self,
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
           item_list = self._get_request(endpoint, search_params)

           return convert_item_list_to_objects(item_list)
    

    def _add_new_user_generated_item(
            self,
            item_type: str,
            data: dict
            ) -> KomgaCollection | KomgaReadlist | KomgaErrorResponse:
        '''
        Post new item

        :param item_type: collections or readlists
        :param data: see docs for data keys
        '''
        return self._post_request(make_endpoint(item_type), json.dumps(data) )
    

    def _update_item_metadata(self, item_type: str, item_id: str, data: dict):
        '''
        Updates metadata for series or book

        :param data: see docs for data keys
        '''
        
        data = json.dumps(data)
        endpoint = make_endpoint(item_type, [item_id, 'metadata'])
        r = self._patch_request(endpoint, data, headers={'Content-Type': 'application/json'})
        return r


    def _get_item_poster(self, item_type: str, item_id: str, convert_to_png: bool = True) -> PngImageFile | io.BytesIO | KomgaErrorResponse:
        '''
        Returns png image for an item thumbnail

        :param convert_to_png: False returns raw bytes
        '''
        endpoint = make_endpoint(item_type, [item_id, 'thumbnail'])
        r = self._get_request(endpoint, {'id': item_id}, headers={'accept': 'image/jpeg'})

        # with open('test.png', 'wb') as image:
        #     image.write(r._content)
        if  isinstance(r, KomgaErrorResponse):
            return r
        elif convert_to_png:  
            return Image.open(io.BytesIO(r._content))
        else: 
             return io.BytesIO(r._content)


    def _get_file(
            self,
            item_type: str,
            item_id: str,
            convert_to_zip: bool = True
            ) -> zipfile.ZipFile | io.BytesIO | KomgaErrorResponse:
        '''
        Returns files as a zip(cbz) file or Bytes object. 

        :param convert_to_zip: True returns a zip file, False returns Bytes object 
        '''

        endpoint = make_endpoint(item_type, [item_id, 'file'])
        r = self._get_request(endpoint, {make_param_key(item_type): item_id})
        if isinstance(r, KomgaErrorResponse):
            return r
        
        elif convert_to_zip:
            return zipfile.ZipFile(io.BytesIO(r._content), 'r')
        else:
            return r._contnet
        

    def _save_file(self, item_type: str, item_id: str, path: str) -> None:
        '''
        Saves the item to path

        :param path: path to save location including name and extention
        '''
        endpoint = make_endpoint(item_type, [item_id, 'file'])
        r = self._get_request(endpoint, {make_param_key(item_type): item_id})

        with open(path, 'wb') as file:
            file.write(r._content)

    def _delete_item_from_library(self, item_type, item_id):
        '''
        Deletes item (this cannot be undone)
        '''
        endpoint = make_endpoint(item_type, item_id)
        return self._delete_request(endpoint)

    def _delete_item_file():
        '''
        Deletes item file (this cannot be undone)
        '''
        pass

    def _get_thumbnails(self, item_type, item_id):
        endpoint = make_endpoint(item_type, [item_id, 'thumbnails'])
        return self._get_request(endpoint, {make_param_key(item_type): item_id})





    