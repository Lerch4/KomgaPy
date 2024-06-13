from komgapy.response_classes import  KomgaSeries, KomgaBook, KomgaCollection, KomgaReadlist, KomgaLibrary


def convert_response_to_komga_item(data):
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


def convert_item_list_to_objects(data) -> (
        KomgaSeries |
        KomgaBook |
        KomgaCollection | 
        KomgaReadlist |
        KomgaLibrary
        ):
    

    if type(data) is not list or not data:
        return data

    obj_list = []
    match convert_response_to_komga_item(data[0]):
        case KomgaSeries():
            for i in data:
                obj_list.append(KomgaSeries(i))
        case KomgaBook():
            for i in data:
                obj_list.append(KomgaBook(i))
        case KomgaCollection():
            for i in data:
                obj_list.append(KomgaCollection(i))
        case KomgaReadlist():
            for i in data:
                obj_list.append(KomgaReadlist(i))
        case KomgaLibrary():
            for i in data:
                obj_list.append(KomgaLibrary(i))
        case _:
            return data

    return obj_list
 