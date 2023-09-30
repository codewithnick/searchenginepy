# searchenginepy

Make search engine queries within your python applications. Searchenginepy allows you to query some of the most common search engines. 

# How to use?

First install searchenginepy and then import it into your project. After importing, you can make queries on the four support search engines. Once a query has been made, a list of the top results will be returned. Initially it configured to display the top results but you are able to select which page you woud like to see in your list. 

## Installation

`pip install searchenginepy`

## Importing

```
from searchenginepy import SearchEngine
engine=SearchEngine()
```

## Usage

If you want to use multiple search engine in your project then you can use the SearchEngine() class to access all four available search engines

```
list=engine.search("search query")
```

## Example

```
list=engine.google("search query")
```

using google to search a query

## Using a specific search engine

You can also create instances of specific search engines to be used throughout your project. This will only give you access to that engine unlike the SearchEngine() class.

### google

```
from searchenginepy.Google import Google
list=Google().search("search query")
```

### Bing

```
from searchenginepy.Bing import Bing
list=Bing().search("search query")
```

### Brave

```
from searchenginepy.Brave import Brave
list=Brave().search("search query")
```

### DuckDuckGo

```
from searchenginepy.DuckDuckGo import DuckDuckGo
list=DuckDuckGo().search("search query")
```
## Example with only HTTPS results

```
from searchenginepy.Google import Google
Google.httpallowed = false

results=Google().search("search query")
```

## Example Specifying page

```
from searchenginepy.Google import Google
results=Google().search("search query", 3)
```
### here we are selecting the third page

## Supported search engines

- Google
- Bing
- DuckDuckGo
- Brave

## Example script

[example.py](./src/example.py)
