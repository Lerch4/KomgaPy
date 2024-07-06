# KomgaPy

KomgaPy is an incomplete Komga API wrapper for python. KomgaPy is still under development and has not been thoroughly tested. Currently KomgaPy has the ability to

- get data from Komga series, books, collections, readlists, libraries
- post new collection and readlists
- overwrite current collections and readlists
- edit / update metadata for series and books
- update poster art from file path
- scan, analyze, and refresh libraries
- utilize data objects for Komga series, books, collections, readlists, searches, and errors


## **Instalation**
- Currently KomgaPy has to be downloaded and installed manually
	- Eventually will be added to PyPI 
	- Download and extract repo to directory and install directory to pip

```
pip install <location of KomgaPy directory>
```

## **Usage**

- KomgaPy is used by creating an instance of a KomgaSession and utilizing its methods to access the Komga API. KomgaSession takes the host URL address of the Komga server and a tuple of the username and password of your account.

```
from komgapy import KomgaSession
session = KomgaSession(komga_url, (user, password))
```

See docs for further usage examples.