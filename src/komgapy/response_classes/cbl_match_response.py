from komgapy.response_classes import KomgaResponse

def convert_match_list(matches: list):
    export_list = []
    for match in matches:
        export_list.append(matched(match))


class series_match():
    def __init__(self, data) -> None:
        series_id = data['seriesId']
        title = data['title']
        release_date: str = data['releaseDate']

class book_match():
    def __init__(self, data) -> None:
        book_id: str = data['bookId']
        number: str = data['number']
        title: str = data['title']

class matched():
    def __init__(self, data) -> None:
        series = data['series']
        books = data['books']


class match_request():
    def __init__(self, data) -> None:
        self.series: list = data['series']
        self.number = data['number']


class match_requests():
    def __init__(self, data) -> None:
        self.request = match_request(data['request'])
        self.matches= matched(data['matches'])


class cbl_match_response(KomgaResponse):
    def __init__(self, match_response_data: dict) -> None:
        self.read_list_match = match_response_data['readListMatch']
        self.requests = match_requests(match_response_data['requests'])
        self.error_code = match_response_data['errorCode']
        self.book_ids = get_book_ids(self.requests)
    
def get_book_ids(requests):
    book_ids = []
    for request in requests:
        if len(request['matches'])>1:
            # for match in request['matches']:
            pass
        else:
            matched_request = request['matches'][0]
            if len(matched_request['books'])> 1: pass
            else: 
                book_ids.append(matched_request['books'][0]['bookId'])
    return book_ids




# def test(t):
#     for 