# KomgaPy

KomgaPy is an incomplete Komga API wrapper for python. KomgaPy is still under development and has not been thoroughly tested.

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
- [ ] Ability to add readlists from .cbl file

## **Installation**
- Currently KomgaPy has to be downloaded and installed manually
	- Eventually will be added to PyPI 
	- Download and extract repo to directory and install directory to pip

```
pip install <KomgaPy file path>
```

## **Usage**

- KomgaPy is used by creating an instance of a KomgaSession and utilizing its methods to access the Komga API. KomgaSession takes the host URL address of the Komga server and a tuple of the username and password of your account.

```
from komgapy import KomgaSession
session = KomgaSession(komga_url, (user, password))
```

See [docs](./docs/) for further usage examples.
