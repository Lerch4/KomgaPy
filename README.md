# KomgaPy

KomgaPy is an incomplete [Komga](https://komga.org/) API wrapper for python. KomgaPy is still under development and has not been thoroughly tested.

### Currently KomgaPy has the ability to

- Get data from series, books, collections, readlists, and libraries
- Search for series, books, collections, and readlists
- Post new collection and readlists
- Overwrite current collections and readlists
- Edit / update metadata for series and books
- Update poster art from file path
- Scan, analyze, and refresh libraries
- Get thumbnail images for series, books, collections, and readlists
- Get files for series, books, and readlists
- Ability to match books from .cbl
	- can match cbl from path or url
- Delete readlists and collections from library

### To Do
- [X] Refactor methods with better class structure and naming
	- all methods have changed
- [ ] Add more endpoints	
- [ ] First Alpha Release


## **Installation**
- Currently KomgaPy has to be installed from github
	- Eventually will be added to PyPI 

```
pip install git+https://github.com/Lerch4/KomgaPy
```

## **Usage**

- KomgaPy is used by creating an instance of a KomgaSession and utilizing its methods to access the Komga API. KomgaSession takes the host URL address of the Komga server and a tuple of the username and password of your account.

```
from komgapy import KomgaSession
session = KomgaSession(komga_url, (user, password))

series = session.series.get(series_name='Batman (2011)')
series.print_data(indent = 2)
```

See [docs](./docs/) for further usage examples.
