# KomgaPy

KomgaPy is an incomplete [Komga](https://komga.org/) API wrapper for python. KomgaPy is still under development and has not been thoroughly tested.

### Currently KomgaPy has the ability to

- get data from series, books, collections, readlists, and libraries
- search for series, books, collections, and readlists
- post new collection and readlists
- overwrite current collections and readlists
- edit / update metadata for series and books
- update poster art from file path
- scan, analyze, and refresh libraries
- get thumbnail images for series, books, collections, and readlists
- get files for series, books, and readlists

### Still to be implemented
- [x] Ability to match books from .cbl file
	- [ ] Make it easier to use matched book data

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
```

See [docs](./docs/) for further usage examples.
