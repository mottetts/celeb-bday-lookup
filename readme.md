# Celebrity Birthday Lookup
## version 0.1

A script that looks up the Wikipedia page of a famous person 
and returns their birthday...

This is still a preliminary (and very buggy) program and only works 
with exact name matches (although Wikipedia's redirect algorithm tends 
to be lenient with punctuation). 

Use a descriptor in parentheses to find celebrities with common 
or ambiguous names, e.g.: 

_Michael Johnson (athlete)_
_Prince (singer)_

The program uses Python libraries requests and Beautiful Soup 4 (bs4) 
to retrieve the web pages and parse them, respectively. 
