from komgapy.response_classes import  KomgaSeries, KomgaBook, KomgaCollection, KomgaReadlist, KomgaLibrary


def convert_response_to_komga_object(data):
    if 'number' in data:
        return KomgaBook(data)
    
    elif 'booksCount' in data:
        return KomgaSeries(data)
    
    elif 'seriesIds' in data:
        return KomgaCollection(data)
    
    elif 'bookIds' in data:
        return KomgaReadlist(data)
    
    elif 'root' in data:
        return KomgaLibrary(data)