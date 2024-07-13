from komgapy.response_classes.komga_response import KomgaResponse


class KomgaBookMetadata(KomgaResponse):
    def __init__(self, series_metadata: dict) -> None:

        self.title = series_metadata['title']
        self.title_lock = series_metadata['titleLock']
        self.summary = series_metadata['summary']
        self.summary_lock = series_metadata['summaryLock']
        self.number = series_metadata['number']
        self.number_lock = series_metadata['numberLock']
        self.number_sort = series_metadata['numberSort']
        self.number_sort_lock = series_metadata['numberSortLock']
        self.release_date = series_metadata['releaseDate']
        self.release_date_lock = series_metadata['releaseDateLock']
        self.authors = series_metadata['authors']
        self.authors_lock = series_metadata['authorsLock']
        self.tags = series_metadata['tags']
        self.tags_lock = series_metadata['tagsLock']
        self.isbn = series_metadata['isbn']
        self.isbn_lock = series_metadata['isbnLock']
        self.links = series_metadata['links']
        self.links_lock = series_metadata['linksLock']
        self.created = series_metadata['created']
        self.last_modified = series_metadata['lastModified']
