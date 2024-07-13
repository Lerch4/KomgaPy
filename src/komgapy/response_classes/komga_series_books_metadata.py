from komgapy.response_classes.komga_response import KomgaResponse


class KomgaSeriesBookMetadata(KomgaResponse):
    def __init__(self, book_metadata: dict) -> None:
        self.authors = book_metadata['authors']
        self.tags = book_metadata['tags']
        self.release_date = book_metadata['releaseDate']
        self.summary = book_metadata['summary']
        self.summary_number = book_metadata['summaryNumber']
        self.created = book_metadata['created']
        self.last_modified = book_metadata['lastModified']

