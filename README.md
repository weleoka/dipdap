Genre is in a list of tuples because lists stay ordered by index... Like this we can add to the genre list later. The valid genre vs. sub-genre should be in a database relation or at least a file so dynamic addition of genra is possible.

The function for generating html from genre list is noteworthy and avoids having to sort the list in any way, and also makes adding to it very easy.

Because the form elements are at base a python dictionary they can appear in any order on a form. For the developer to decide which order the elements are output, the element header is "el-[integer]". Where 'integer' is then incremented and defines order in an ascending or descending manner.


### DipDap versions
v0.0.1 (current)

(Note to author: version specified in:
    main.config, 
    README.md, 
    CHANGELOG.md, 
    repository tag)



### Requirements
Python 3.4


### Overview
DipDap - a simple tool to manage a library database.

DipDap can add books to a database. Users can also rate the book and assign it a genre and sub-genre.

The default database file is a CSV file.
This will later be able to be changed in the config part of dipdap.

An entry in the database takes the form:

Title, Author, Genre, Genre2, Date finished, Score, Comments

The score is simply from 1 - 5.

Genre is simply genre.

Genre2 is what type of book under that genre. So under fiction there could be horror, teen, detektive, fantasy, sci-fi etc. Under textbooks/fact-books there could be engineering, mathematics, biology and computer science for example.

Please report any issues to kawe009@nothing.yet



### Installation
1. Git clone or download archive and extract.
2. Make dipdap executable
3. Run as shell script "./dipdap" or make global and run dipdap.


### Usage



### Current Features:
General functinality:

Specs and options:



### Bugs, known Issues and missing Features:

Please report an issue if one is found.

Functionality:

Specs and options:

Security:

Code, style and performance:



### Contributing

If you'd like to contribute to DipDep's development, start by forking the GitHub repo:

https://github.com/weleoka/dipdep.git

Have a look at the known issues and missing features and take a pick or find something else that needs doing. 
You jump right on the wishlist/joblist by finding tagged items in the source code. Run pydoc and then searching for the '#->' tags! 

The best way to get your changes merged is as follows:

1. Clone your fork
2. Hack away
3. If you are adding significant new functionality, document it in the README
4. Do not change the version number, I will do that on my end
5. Push the repo up to GitHub
6. Send a pull request to [weleoka/dipdap](https://github.com/weleoka/dipdap)



### Licence

GNU GENERAL PUBLIC LICENSE

LICENCE.md for details.

Copyright (c) 2016 A.K. Weeks



### Sources, inspiration and notes
Credits go to docs.python.org, stackoverflow.com

