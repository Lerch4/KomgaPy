from komgapy.response_classes import KomgaItem



class KomgaLibrary(KomgaItem):
    def __init__(self, library_data: dict) -> None:
        super().__init__(library_data)
        self.root = library_data['root']
        self.import_comic_info_book = library_data['importComicInfoBook']
        self.import_comic_info_series = library_data['importComicInfoSeries']
        self.import_comic_info_collection = library_data['importComicInfoCollection']
        self.import_comic_info_readlist = library_data['importComicInfoReadList']
        self.import_comic_info_series_append_volume = library_data['importComicInfoSeriesAppendVolume']
        self.import_epub_book = library_data['importEpubBook']
        self.import_epub_series = library_data['importEpubSeries']
        self.import_mylar_series = library_data['importMylarSeries']
        self.import_local_artwork = library_data['importLocalArtwork']
        self.import_barcode_isbn = library_data['importBarcodeIsbn']
        self.scan_force_modified_time = library_data['hashFiles']
        self.scan_interval = library_data['scanInterval']
        self.scan_on_startup = library_data['scanOnStartup']
        self.scan_cbx = library_data['scanCbx']
        self.scan_pdf = library_data['scanPdf']
        self.scan_epub = library_data['scanEpub']
        self.scan_directory_exclusions = library_data['scanDirectoryExclusions']
        self.repair_extensions = library_data['repairExtensions']
        self.convert_to_cbz = library_data['convertToCbz']
        self.empty_trash_after_scan = library_data['emptyTrashAfterScan']
        self.series_cover = library_data['seriesCover']
        self.hash_files: bool = library_data['hashFiles']
        self.hash_pages: bool = library_data['hashPages']
        self.analyze_dimensions = library_data['analyzeDimensions']
        self.one_shots_directory = library_data['oneshotsDirectory']
        self.unavailable = library_data['unavailable']
