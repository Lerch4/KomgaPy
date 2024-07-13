from komgapy.response_classes import KomgaResponse


class cbl_match_response(KomgaResponse):
    def __init__(self, match_response_data: dict) -> None:
        self.read_list_match = match_response_data['readListMatch']
        self.requests = match_response_data['requests']
        self.error_code = match_response_data['errorCode']
        (self.book_ids, self.unmatched, self.multi_match) =  validate_match_data(self.requests)
    

def validate_match_data(requests):
    '''
    Parse match data
    '''
    book_ids = []
    no_match = []
    multi_match = []
    matched: bool = False
    for request in requests:

        match len(request['matches']):
            case 0:
                no_match.append(request)
                continue
            case 1: pass
            case _:
                multi_match.append(request)

        request_string_part = request['request']['series'][0].split(')')
        request_release_year = request_string_part[0].split('(')[1]

        for i, m in enumerate(request['matches']):
            match_release_year = m['series']['releaseDate'].split('-')[0]
            if  match_release_year == request_release_year:

                matched_request = request['matches'][i]

                matched_request = matched_request = request['matches'][i]

                matched = True
                continue

        if not matched:
            no_match.append(request)
            continue

        match len(matched_request['books']):
            case 0:
                no_match.append(request)
                continue
                
            case 1: pass
            case _:
               multi_match.append(request)

        book_ids.append(matched_request['books'][0]['bookId'])

    return (book_ids, no_match, multi_match)