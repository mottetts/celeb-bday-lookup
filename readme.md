# Wiki-birthday 0.1

A script that looks up the Wikipedia page of a famous person 
and returns their birthday...

![Wiki-birthday screenshot](screenshot.PNG)

This program is in early development and only works with exact name 
matches (although Wikipedia's redirects tend to be 
lenient with punctuation). Famous people without exact known birthdays
aren't searchable.

Use a descriptor in parentheses to find celebrities with common 
or ambiguous names, e.g.: 

_Michael Johnson (athlete)_

_Prince (singer)_

The program uses Python libraries `requests` and `Beautiful Soup 4 (bs4)` 
to retrieve the web pages and parse them, respectively. 
