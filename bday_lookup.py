# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 20:04:08 2019

@author: motec
"""

from datetime import datetime
import requests
from bs4 import BeautifulSoup

#normalize capitalization of string for easier lookup
def normCaps(name):
    y = []
    x = name.split()
    for i in range(len(x)):
        y.append(x[i].capitalize())
    newname = ' '.join(y)
    return newname

#check if the URL is a disambiguation page
def disambig(bs):
    if bs.find("table", id="disambigbox") == None:
        return False
    else:
        return True

#look up name as stored in first heading of page and birthday
#return none if no birthday available
def birthday(res):
    try:
        bs = BeautifulSoup(res.text, 'lxml')
        date = bs.find("span", class_="bday").text
        name = bs.find("h1", class_="firstHeading").text
        ndate = datetime.strptime(date, '%Y-%m-%d')
        return name,ndate.strftime("%B %d, %Y")
    except:
        return None,None

print(
    '''
Enter the name of a famous person with a Wikipedia page to look up 
their birthday. Type Q to quit.
    ''')

while True:
    name = normCaps(input('> '))
    if name == 'Q': break

    url = 'https://en.wikipedia.org/wiki/'+name
    res = requests.get(url)
    
    if res.status_code == 200:
        bs = BeautifulSoup(res.text, 'lxml')
        if disambig(bs):
            print('''
Can't find a page for that person. You might want to try a more specific name 
or include a descriptor in parentheses (ex. "George W. Bush", "Madonna (entertainer)")
                  ''')
        else:
            wikiname,bday = birthday(res)
            if bday != None:
                print(wikiname, "was born on", bday + ".")
            else:
                print("There doesn't seem to be a birthday associated with that name.")
    else:
        print("Sorry, there is no record for that person or the page doesn't exist.")