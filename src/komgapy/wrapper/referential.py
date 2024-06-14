from komgapy.util import make_endpoint


def list_referential(self, reference, second_reference = None, search_params = None):

        endpoint = make_endpoint(reference, second_reference)
        return self._get_request(endpoint, search_params)
