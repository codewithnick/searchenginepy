# searchenginepy

search engine for python (Query and scrape search engines)

# How to use?

## Installation

`pip install searchenginepy`

## Importing

```
import SearchEngine from searchenginepy
engine=SearchEngine()
```

## Usage

```
list=engine.search("search query")
```

## Example

```
list=engine.google("search query")
```

using google to search a query

## Using a specific search engine

### google

```
from searchenginepy import Google
list=Google().search("search query")
```

### Bing

```
from searchenginepy import Bing
list=Bing().search("search query")
```
### Brave
```
from searchenginepy import Brave
list=Brave().search("search query")
```

### DuckDuckGo

```
from searchenginepy import DuckDuckGo
list=DuckDuckGo().search("search query")
```

## Supported search engines

- Google
- Bing
- DuckDuckGo
- Brave
