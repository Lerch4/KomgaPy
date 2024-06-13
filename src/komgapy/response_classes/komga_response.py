import json

class KomgaResponse:
    def print_data(self, indent: int = None, seperators: tuple = None) -> None:
        '''
        Prints the objects data in JSON format, including nested object data. 

        :param indent: Data will be pretty-printed with that indent level. An indent level of 0 will only insert newlines. None is the most compact representation. Only positive integers. (Taken from JSON.dumps)
        :param separators: Characters to seperate items and keys. Used in (item_separator, key_separator) format. The default is (', ', ': ') (Taken from JSON.dumps)
        '''
        print(
            json.dumps(
                vars(self),
                indent=indent,
                separators=seperators,
                default=lambda obj: vars(obj)
                )
            )
