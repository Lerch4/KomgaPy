from komgapy.response_classes import KomgaItem
from komgapy.response_classes.komga_series_metadata import KomgaSeriesMetadata

class KomgaSeries(KomgaItem):
    def __init__(self, series_data: dict) -> None: 
        super().__init__(series_data)
        self.library_id = series_data['libraryId']
        self.url = series_data['url']
        self.created = series_data['created']
        self.last_modified = series_data['lastModified']
        self.file_last_modified = series_data['fileLastModified']
        self.books_count = series_data['booksCount']
        self.books_read_count = series_data['booksReadCount']
        self.books_unread_count = series_data['booksUnreadCount']
        self.books_in_progress_count = series_data['booksInProgressCount']
        # self.metadata = series_data['metadata']
        self.book_metadata = series_data['booksMetadata']
        self.deleted = series_data['deleted']
        self.oneshot = series_data['oneshot']
        self.metadata = KomgaSeriesMetadata(series_data['metadata'])

