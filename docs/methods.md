### List of Methods

 [Series Methods](/src/komgapy/wrapper/series.py)
- `get_series()`
- `search_series()`
- `update_series_metadata()`
- `series_in_collection()`
- `get_series_poster()`
- `get_series_files()`
- `save_series_files()`

[Book Methods](/src/komgapy/wrapper/book.py)
- `get_book()`
- `search_book()`
- `update_book_metadata()`
- `books_in_series()`
- `books_in_readlist()`
- `get_book_poster()`
- `get_book_files()`
- `save_book_file()`

[Collection Methods](/src/komgapy/wrapper/collection.py)
- `get_collection()`
- `search_collection()`
- `add_new_collection()`
- `overwrite_existing_collection()`
- `update_collection_poster()`
- `collections_in_series()`
- `get_collection_poster()`

[Readlist Methods](/src/komgapy/wrapper/readlist.py)
- `get_readlist()`
- `search_readlist()`
- `add_new_readlist()`
- `overwrite_existing_readlist()`
- `update_readlist_poster()`
- `get_readlist_poster()`
- `get_readlist_files()`
- `save_readlist_files()`
- `match_readlist_cbl()`
- `match_readlist_cbl_from_path()`

[Library Methods](/src/komgapy/wrapper/library.py)
- `list_all_libraries()`
- `get_library()`
- `update_library()`
- `analyze_library()`
- `empty_library_trash()`
- `refresh_library_metadata()`
- `scan_library()`

[Referential Methods](/src/komgapy/wrapper/referential.py)
- `list_referential()`
---
### Method Examples

- #### Get methods
    - `get_series(), get_book(), get_collection(), get_readlist(), get_library()`
    - Returns single Komga object
    - Takes either id or name with id being preferred. Name returns first search result that matches name exactly

```
series = session.get_series('0ABC123XY45Z1')
series.print_data()
```

```
series = session.get_series(series_name='Batman (2011)')
series.print_data(indent = 2)
```


---
- #### Search methods
	- `search_series(), search_book(), search_collection(), search_readlist()`
	- Returns `KomgaSearchResponse` that will contain a list of Komga objects as well as data on the search
		- List of Komga objects will be in the `content` attribute of the search response instance
	- Takes a dictionary of search parameters that are different for each type of Komga object
		- Search is the most used parameter and most of the other parameters can be made redundant by using[ Full Text Search](https://komga.org/docs/guides/search/).  All parameters are taken from the Komga API and not all have been tested. 
	    - Available parameters (from [Komga API](https://komga.org/docs/api/rest))
		    - Series
		        - search: `string`
					<!-- - Komga Full Text Search -->
		        - library_id : `list[string] | string`
					<!-- - Komga ID(s) for libraries to search from. Left blank will search all libraries. -->
		        - collection_id : `list[string] | string`
					<!-- - Komga ID(s) for collections to search from. -->
		        - status : `'ENDED' | 'ONGOING' | 'ABANDONED' | 'HIATUS'`
		        - read_status : `'UNREAD' | 'READ' | 'IN_PROGRESS'`
		        - publisher : `list[string] | string`
		        - language : `list[string] | string`
		        - genre : `list[string] | string`
		        - tag: `list[string] | string`
		        - age_rating: `list[string] | string`
		        - release_year: `list[string] | string`
		        - sharing_label: `list[string] | string`
		        - deleted: `bool`
		        - complete: `bool`
		        - oneshot: `bool`
		        - unpaged: `bool`
		        - default - `False`
		        - search_regex: `string`
		        - page: `integer`
		        - size: `integer`
		        - sort: `list[string] | string`
		        - author: `list[string] | string`
			- Book
				- search: `string`
				- library_id: `list[string]`
				- media_status: `UNKNOWN, ERROR, READY, UNSUPPORTED, OUTDATED`
				- read_status : `UNREAD, READ, IN_PROGRESS`
				- released_after: `string($date)`
				- tag: `list[string]`
				- unpaged: `bool`
				- page: `intger`
				- size: `integer`
				- sort: `list[string]`
			- Collection
				- search: `string`
				- library_id: `list[string]`
				- unpaged: `bool`
				- page: `intger`
				- size: `integer`
			- ReadList
				- search: `string`
				- library_id: `list[string]`
				- unpaged: `bool`
				- page: `intger`
				- size: `integer`


```
search_response = session.search_series({'search': '"Walking Dead"', 'unpaged': True})
search_response.print_data()
```

```
search_response = session.search_series({'search': '"Walking Dead"', 'unpaged': True})
series_list = search_response.content
for series in series_list:
	print(f'Name: {series.name}\nID  : {series.id}\n')
```

- ##### Full Text Search vs Search Parameters
	- Both examples below return the same result
```
search_response = session.search_series({'search': 'publisher: Image', 'unpaged': True})
print(search_response.number_of_elements)
```

```
search_response = session.search_series({'publisher': 'Image', 'unpaged': True})
print(search_response.number_of_elements)
```
---
- #### Adding new Collections and Readlists
	- `add_new_collection(), add_new_readlist()`
	- Takes data as a dictionary 
```
new_collection_data = {
	'name': 'new collection',
	'ordered': False,
	'seriesIds': [0ABC123XY45Z1, 0ABC123XY45Z2, 0ABC123XY45Z3]
	}

session.add_new_collection(new_collection_data)
```

```
new_readlist_data = {
	'name' : 'new_readlist',
	'ordered': False,
	'summary': 'New readlist example.'
	'bookIds': [0ABC123XY45Z1, 0ABC123XY45Z2, 0ABC123XY45Z3]
	}

session.add_new_readlist(new_readlist_data)
```
---
- #### Additional Method Examples
```
collection = session.get_collection(collection_name='{2}: Nightwing')
series_list = session.series_in_collection(collection.id)
for series in series_list:
	series.print_data()

```

```
session.update_series_metadata(series.id, {'status': 'ENDED'})
```

```
session.update_collection_poster(collection.id, file_path)
```

```
series_list = session.series_search({'search':'reading_direction:right_to_left'}).content
```
