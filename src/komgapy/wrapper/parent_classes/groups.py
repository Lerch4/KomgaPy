import json


from komgapy.util import make_endpoint
from komgapy.wrapper.request_adapter import RequestAdapter
from komgapy.response_classes import (
    KomgaCollection,
    KomgaReadlist,
    KomgaErrorResponse,
    )


class Groups():
    '''
    Groups Parent Class.
    Contains methods relivent only to collections and readlists.
    '''
    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None:
        self._ra = RequestAdapter(komga_url, auth)


    def overwrite(self, item_type: str, item_id: str, data: dict):
            '''
            Replaces current data with new data for collections or readlists
            '''
            return self._ra._patch_request(make_endpoint(item_type, [item_id]), json.dumps(data))


    def new(
            self,
            item_type: str,
            data: dict
            ) -> KomgaCollection | KomgaReadlist | KomgaErrorResponse:
        '''
        Post new item

        :param item_type: collections or readlists
        :param data: see docs for data keys
        '''
        return self._ra._post_request(make_endpoint(item_type), json.dumps(data) )



    def remove(self, item_type, item_id):
        '''
        Deletes item (this cannot be undone)
        '''
        endpoint = make_endpoint(item_type, item_id)
        return self._ra._delete_request(endpoint)
