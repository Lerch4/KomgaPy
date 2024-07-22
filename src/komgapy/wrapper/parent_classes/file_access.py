import io, zipfile

from komgapy.response_classes import  KomgaErrorResponse
from komgapy.wrapper.request_adapter import RequestAdapter
from komgapy.util import make_endpoint, make_param_key




class FileAccess:

    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None:
        self._ra = RequestAdapter(komga_url, auth)

    def files(
            session,
            item_type: str,
            item_id: str,
            convert_to_zip: bool = True
            ) -> zipfile.ZipFile | io.BytesIO | KomgaErrorResponse:
        '''
        Returns files as a zip(cbz) file or Bytes object. 

        :param convert_to_zip: True returns a zip file, False returns Bytes object 
        '''

        endpoint = make_endpoint(item_type, [item_id, 'file'])
        r = session._ra._get_request(endpoint, {make_param_key(item_type): item_id})
        if isinstance(r, KomgaErrorResponse):
            return r
        
        elif convert_to_zip:
            return zipfile.ZipFile(io.BytesIO(r._content), 'r')
        else:
            return r._contnet
        

    def save_files(session, item_type: str, item_id: str, path: str) -> None:
        '''
        Saves the item to path

        :param path: path to save location including name and extention
        '''
        endpoint = make_endpoint(item_type, [item_id, 'file'])
        r = session._ra._get_request(endpoint, {make_param_key(item_type): item_id})

        with open(path, 'wb') as file:
            file.write(r._content)

