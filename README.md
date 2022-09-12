# NLP Portfolio
Portfolio to showcase work from CS 4395 (Natural Language Processing)

## Overview of NLP
In this [overview of NLP](overview_of_NLP.pdf), I define NLP, describe the relationship between AI and NLP, compare and contrast natural language understanding and natural language generation, list some examples of modern NLP applications, describe the 3 main approaches to NLP with examples, and describe my personal interest in NLP.

## Assignment 1: Text Processing
[This program](text_processing.py) reads in an [employee file](data.csv), processes the text to be more standardized, creates an object for each person with corrections from the user, and displays the information of each person.

This program can be run on the Python terminal by entering the name of the program with the relative path *data/data.csv* as a system argument, where [data.csv](data.csv) is the file that should be located inside a folder named *data*. Example: text_processing.py data/data.csv

Python is useful for text processing because it has modules like the Natural Language Toolkit (NLTK) library with functions to process text easily, such as parsing using tokens. Python's weakness when it comes to text processing is that an interpreted language like Python can run slow for programs that require processing large amounts of data.

Through this assignment, I learned how to work with regular expressions to process text to match a specific format and with pickling/unpickling to save a dictionary of employee data to file for reading. I also reviewed sysarg, file I/O, and creating classes in Python.

## Assignment 2: Exploring NLTK
[This Python notebook](exploring_NLTK.pdf) explores the NLTK library in Python for performing NLP functions such as tokenizing and text preprocessing like stemming and lemmatization.
