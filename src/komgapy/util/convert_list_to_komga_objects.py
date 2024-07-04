from komgapy.response_classes import  KomgaSeries, KomgaBook, KomgaCollection, KomgaReadlist, KomgaLibrary
from komgapy.util.convert_data_to_komga_object import convert_response_to_komga_object




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
    match convert_response_to_komga_object(data[0]):
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
 