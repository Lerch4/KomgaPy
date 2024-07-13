from komgapy.response_classes import KomgaItem
from komgapy.response_classes.komga_book_metadata import KomgaBookMetadata

class KomgaBook(KomgaItem):
    def __init__(self, book_data: dict) -> None:
        super().__init__(book_data)
        self.series_id = book_data['seriesId']
        self.series_title = book_data['seriesTitle']
        self.library_id = book_data['libraryId']
        self.url = book_data['url']
        self.number = book_data['number']
        self.created = book_data['created']
        self.last_modified = book_data['lastModified']
        self.size_bytes = book_data['sizeBytes']
        self.size = book_data['size']
        self.media = book_data['media']
        self.metadata = KomgaBookMetadata(book_data['metadata'])
