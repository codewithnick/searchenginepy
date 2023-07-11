##################################################################
#                       IMPORTING MODULES
##################################################################
from searchenginepy.Bing import Bing
from searchenginepy.Google import Google
from searchenginepy.DuckDuckGo import Duckduckgo
from searchenginepy.Brave import Brave
from searchenginepy import SearchEngine
################################################################
PAGE_NUMBER=1
TOP_RESULT_STRING='Top result for page number:'
################################################################
#                       USING SEARCH ENGINE CLASS
###############################################################
searchengine = SearchEngine('search engine',PAGE_NUMBER)
obj1=searchengine.google()
obj2=searchengine.bing()
obj3=searchengine.duckduckgo()
obj4=searchengine.brave()
print(TOP_RESULT_STRING,PAGE_NUMBER,' from google:',obj1[0])
print(TOP_RESULT_STRING,PAGE_NUMBER,' from bing:',obj2[0])
print(TOP_RESULT_STRING,PAGE_NUMBER,' from duckduckgo:',obj3[0])
print(TOP_RESULT_STRING,PAGE_NUMBER,' from brave:',obj4[0])
#################################################################
#                       USING SPECIFIC SEARCH ENGINES
#################################################################
PAGE_NUMBER=2
googleobj=Google()
res=googleobj.search('google',PAGE_NUMBER)
print(TOP_RESULT_STRING,PAGE_NUMBER,' from google:',res[0])
braveobj=Brave()
res=braveobj.search('brave',PAGE_NUMBER)
print(TOP_RESULT_STRING,PAGE_NUMBER,' from brave:',res[0])
duckduckgoobj=Duckduckgo() 
res=duckduckgoobj.search('duckduckgo',PAGE_NUMBER)
print(TOP_RESULT_STRING,PAGE_NUMBER,' from duckduckgo:',res[0])
bingobj=Bing()
res=bingobj.search('bing',PAGE_NUMBER)
print(TOP_RESULT_STRING,PAGE_NUMBER,' from bing:',res[0]) 
