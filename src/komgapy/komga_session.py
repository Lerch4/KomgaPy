from komgapy.wrapper.controllers import*


class KomgaSession():
    '''
    Wrapper session class for Komga API requests.

    :param komga_url: host url for komga server
    :param auth: username and password
    '''
    def __init__(self, komga_url: str, auth: tuple[str,str]) -> None: 

        self.readlists = Readlists(komga_url, auth)
        self.series = Series(komga_url, auth)
        self.books = Books(komga_url, auth)
        self.collections = Collections(komga_url, auth)
        self.libraries = Libraries(komga_url, auth) 
        self.referential = Referential (komga_url, auth)

#------------------------------------