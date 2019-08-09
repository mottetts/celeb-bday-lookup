# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 20:04:08 2019

@author: motec
"""

from datetime import datetime
import requests
from bs4 import BeautifulSoup

def birthday(res):
    try:
        bs = BeautifulSoup(res.text, 'lxml')
        date = bs.find("span", class_="bday").text
        ndate = datetime.strptime(date, '%Y-%m-%d')
        return ndate.strftime("%B %d, %Y")
    except AttributeError:
        return None

print(
    '''
    Enter the name of a famous person with a Wikipedia page 
    to look up their birthday.  Type CTRL+D to quit.
    ''')

while True:
    name = input('> ')

    url = 'https://en.wikipedia.org/wiki/'+name
    res = requests.get(url)
    
    if res.status_code == 200:
        bday = birthday(res)
        if bday != None:
            print(name, "was born on", bday + ".")
        else:
            print("There doesn't seem to be a birthday associated with this person.")
    else:
        print("Sorry, there is no record for that person or the page is currently unavailable.")