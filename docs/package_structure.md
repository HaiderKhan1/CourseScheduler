# Package Layout

## main.py
* main file that will be ran
* house all the cli code 
    * letting users select commands
* call functions from search and parse modules

## search.py
* search is a Class:
* stores class vairables (parsed data)
* has methods to perform search
    * search by course code
    * search by available sections

## parse.py
* set of functions that will parse the html file
* create the JSON file

# How to run code
## Calling Modules
in parse.py there is a function called parseHTML, and we want to access it in the main.py, 
**heres an example:** 
`from modules import parse`
`parse.parseHTML()`

## Developing in python package structure
We do not have to run main.py and import the function from modules for developing and testing
**We can directly run the files in modules for developing as normal**
`python parse.py`


In main.py we can import from modules as:
from modules import search
