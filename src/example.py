##################################################################
#                       IMPORTING MODULES
##################################################################
from searchenginepy.Bing import Bing
from searchenginepy.Google import Google
from searchenginepy.DuckDuckGo import Duckduckgo
from searchenginepy.Brave import Brave
from searchenginepy import SearchEngine
################################################################
PAGE_NUMBER_STRING="Page Number: "
PAGE_NUMBER=1
RESULT_NUMBER_STRING="\nResult Number: "
################################################################
#                       USING SEARCH ENGINE CLASS
###############################################################
searchengine = SearchEngine("searchenginepy",PAGE_NUMBER)
obj1=searchengine.google()
obj2=searchengine.bing()
obj3=searchengine.duckduckgo()
obj4=searchengine.brave()
if(len(obj1)>0):
    print("\n",PAGE_NUMBER_STRING,PAGE_NUMBER,"\n")
    for res,obj in enumerate(obj1):
        print(RESULT_NUMBER_STRING,res)
        print('from google:')
        print(obj)
else:
    print('No results from google')
if(len(obj2)>0):
    print("\n",PAGE_NUMBER_STRING,PAGE_NUMBER,"\n")
    for res,obj in enumerate(obj2):
        print(RESULT_NUMBER_STRING,res)
        print('from bing:')
        print(obj)
else:
    print('No results from bing')
if(len(obj3)>0):
    print("\n",PAGE_NUMBER_STRING,PAGE_NUMBER,"\n")
    for res,obj in enumerate(obj3):
        print(RESULT_NUMBER_STRING,res)
        print('from duckduckgo:')
        print(obj)
else:
    print('No results from duckduckgo')
if(len(obj4)>0):
    print("\n",PAGE_NUMBER_STRING,PAGE_NUMBER,"\n")
    for res,obj in enumerate(obj4):
        print(RESULT_NUMBER_STRING,res)
        print('from brave:')
        print(obj)
else:
    print('No results from brave')
#################################################################
#                       USING SPECIFIC SEARCH ENGINES
#################################################################
PAGE_NUMBER=2

googleobj=Google()
response=googleobj.search('google',PAGE_NUMBER)
if(len(response)>0):
    print("\n",PAGE_NUMBER_STRING,PAGE_NUMBER,"\n")
    for res,obj in enumerate(response):
        print(RESULT_NUMBER_STRING,res)
        print('from google:')
        print(obj)

braveobj=Brave()
response=braveobj.search('brave',PAGE_NUMBER)
if(len(response)>0):
    print("\n",PAGE_NUMBER_STRING,PAGE_NUMBER,"\n")
    for res,obj in enumerate(response):
        print(RESULT_NUMBER_STRING,res)
        print('from brave:')
        print(obj)

duckduckgoobj=Duckduckgo() 
response=duckduckgoobj.search('duckduckgo',PAGE_NUMBER)
if(len(response)>0):
    print("\n",PAGE_NUMBER_STRING,PAGE_NUMBER,"\n")
    for res,obj in enumerate(response):
        print(RESULT_NUMBER_STRING,res)
        print('from duckduckgo:')
        print(obj)

bingobj=Bing()
response=bingobj.search('bing',PAGE_NUMBER)
if(len(response)>0):
    print("\n",PAGE_NUMBER_STRING,PAGE_NUMBER,"\n")
    for res,obj in enumerate(response):
        print(RESULT_NUMBER_STRING,res)
        print('from bing:')
        print(obj)
