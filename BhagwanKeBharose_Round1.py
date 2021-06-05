import requests 
from bs4 import BeautifulSoup as bs
import re

def access():
    tags = {tag.name for tag in soup.find_all()}    
    for tag in tags:
        for i in soup.find_all( tag ):       
            if i.has_attr( "class" ):
                if len( i['class'] ) != 0:
                    class_list.add(" ".join( i['class']))
       
links = ["https://webgeeks-3.herokuapp.com/" , 
         "https://webgeeks-3.herokuapp.com/sonnet1.html",
         "https://webgeeks-3.herokuapp.com/sonnet2.html" , 
         "https://webgeeks-3.herokuapp.com/sonnet3.html",
         "https://webgeeks-3.herokuapp.com/web4.html",
         "https://webgeeks-3.herokuapp.com/web5.html" , 
         ]

class_list= set()

for link in links:    
    r = requests.get(link)
    soup = bs(r.content)
    access()

print( class_list )