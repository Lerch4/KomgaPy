from komgapy.util import make_endpoint

class Referential:
        
    def list_referential(
                self,
                reference: str,
                second_reference: str = None,
                search_params: dict = None
                )-> list[str]:
            '''
            From referential api controller.
            Lists all of a reference.
            :param reference: Type of data to list (see below for list of options)
            :param second_reference: Optional secondary reference for specific primary references. 
            :param: search_params: Additional parameters to narrow down results(see docs for keys).
            
            Primary refereces:
                age-rating, 
                authors,
                genres,
                languages,
                publishers,
                sharing-labels,
                tags,
                series(only with release-dates as second)

            Secondary references:
                tags: books, series
                series: release-dates
                authors: roles, names

            '''

            endpoint = make_endpoint(reference, second_reference)
            return self._get_request(endpoint, search_params)
