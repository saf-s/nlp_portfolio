# NLP Portfolio
Portfolio to showcase work from CS 4395 (Natural Language Processing)

## Overview of NLP
In this [overview of NLP](overview_of_NLP.pdf), I define NLP, describe the relationship between AI and NLP, compare and contrast natural language understanding and natural language generation, list some examples of modern NLP applications, describe the 3 main approaches to NLP with examples, and describe my personal interest in NLP.

## Text Processing
[This program](text_processing/text_processing.py) reads in an [employee file](text_processing/data.csv), processes the text to be more standardized, creates an object for each person with corrections from the user, and displays the information of each person.

The program can be run on the Python terminal by entering the name of the program followed by the relative path *data/data.csv* as a system argument, where [data.csv](text_processing/data.csv) is the file that should be located inside a folder named *data*. Example: text_processing.py data/data.csv

Python is useful for text processing because it has modules like the Natural Language Toolkit (NLTK) library with functions to process text easily, such as parsing using tokens. Python's weakness when it comes to text processing is that an interpreted language like Python can run slow for programs that require processing large amounts of data.

Through this project, I learned how to work with regular expressions to process text to match a specific format and with pickling/unpickling to save a dictionary of employee data to file for reading. I also reviewed system arguments, file I/O, and creating classes in Python.

## Exploring NLTK
[This Python notebook](exploring_NLTK.pdf) explores how the NLTK library in Python can be used for performing NLP functions such as tokenizing and text preprocessing functions like stemming and lemmatization.

## Word Guessing Game
[This program](guessing_game/guessing_game.py) reads in an input file like [anat19.txt](guessing_game/anat19.txt) and preprocesses the text in the file to display lexical diversity, 20 POS tags, number of tokens, number of noun lemmas, and 50 most common words from the file. It then randomly chooses a word from a list of the top 50 words in the preprocessed text and simulates a word guessing game using the random word by prompting the user to guess a letter in the word until the user either guesses the word correctly, runs out of guesses, or exits the game.

The program can be run on the Python terminal by entering the name of the program followed by the filename of the input file as a system argument. Example: guessing_game.py anat19.txt

## Exploring WordNet
[This Python notebook](WordNet.pdf) explores functions of the WordNet lexical database, which connects the semantic relationships between words in English using synonym sets, gloss definitons, usage examples, collocations, and other relations.
