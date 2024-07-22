import json

from komgapy.util import make_endpoint
from komgapy.wrapper.request_adapter import RequestAdapter


class Content:

    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None:
        self._ra = RequestAdapter(komga_url, auth)

    def update_metadata(self, item_type: str, item_id: str, data: dict):
        '''
        Updates metadata for series or book

        :param data: see docs for data keys
        '''
        
        data = json.dumps(data)
        endpoint = make_endpoint(item_type, [item_id, 'metadata'])
        r = self._patch_request(endpoint, data, headers={'Content-Type': 'application/json'})
        return r
