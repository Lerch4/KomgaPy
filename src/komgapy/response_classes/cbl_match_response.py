from komgapy.response_classes import KomgaResponse


class cbl_match_response(KomgaResponse):
    def __init__(self, match_response_data: dict) -> None:
        self.read_list_match = match_response_data['readListMatch']
        self.requests = match_response_data['requests']
        self.error_code = match_response_data['errorCode']
        self.book_ids = get_book_ids(self.requests)
    
# def get_book_ids(requests):
#     book_ids = []
#     for request in requests:
#         if len(request['matches'])>1:
#             print('multiple matches -- selecting first option')
        

#         matched_request = request['matches'][0]

#         if len(matched_request['books'])> 1:
#             print('multiple books -- selecting first option')
 
#         book_ids.append(matched_request['books'][0]['bookId'])

#     return book_ids

def get_book_ids(requests):
    book_ids = []
    for request in requests:

        match len(request['matches']):
            case 0:
                print('No Match')
                continue
            case 1: pass
            case _:
                print('multiple matches -- selecting first option')                

        matched_request = request['matches'][0]

        match len(matched_request['books']):
            case 0:
                print('No Match')
                continue
                
            case 1: pass
            case _:
                print('multiple books -- selecting first option')  
 
        book_ids.append(matched_request['books'][0]['bookId'])

    return book_ids
