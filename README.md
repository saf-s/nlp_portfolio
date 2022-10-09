# NLP Portfolio
Showcasing work for Natural Language Processing (CS 4395)

## Overview of NLP
In [this overview of NLP](overview_of_NLP.pdf), I define NLP, describe the relationship between AI and NLP, compare and contrast natural language understanding and natural language generation, list some examples of modern NLP applications, describe the 3 main approaches to NLP with examples, and describe my personal interest in NLP.

## Text Processing
[This program](text_processing/text_processing.py) reads in an [employee file](text_processing/data.csv) containing information on each person, processes the text into a more standardized format, creates an object for each person after requesting format corrections from the user, and displays the updated information of each person.

The Python program can be run on the terminal by entering a command that has the name of the program followed by the relative path of the input file as a system argument, such as:

*text_processing.py data/data.csv*

where [data.csv](text_processing/data/data.csv) is the file that should be located inside a folder named [data](text_processing/data). 

Python is useful for text processing because it incorporates modules like the Natural Language Toolkit (NLTK) with functions to process text easily, such as parsing using tokens. Python's weakness when it comes to text processing is that an interpreted language like Python can run slow for programs that require processing large amounts of data.

Through this project, I learned how to work with regular expressions to process text to match a specific format. I implemented pickling/unpickling to save a dictionary of employee data to file for safe reading. I also reviewed system arguments, file I/O, and creating dictionaries and classes in Python.

## Exploring NLTK
[This Python notebook](exploring_NLTK.pdf) explores how NLTK interfaces in Python can be used for performing NLP functions such as tokenizing and text preprocessing functions like stemming and lemmatization.

## Word Guessing Game
[This program](guessing_game/guessing_game.py) reads in an input file like [this](guessing_game/anat19.txt) and preprocesses the text in the file to display lexical diversity, 20 POS tags, number of tokens, number of noun lemmas, and 50 most common words from the file. It then randomly chooses a word from a list of the top 50 words in the preprocessed text and simulates a word guessing game using the random word by prompting the user to guess a letter in the word until the user either guesses the word correctly, runs out of guesses, or exits the game.

The program is written in Python and can be run on the terminal by entering the name of the program followed by the filename of the input text file as a system argument.

Example command line: *guessing_game.py anat19.txt*

## Exploring WordNet
[This Python notebook](WordNet.pdf) explores functions of the WordNet lexical database, which connects the semantic relationships between words in English using synonym sets, gloss definitions, usage examples, collocations, and other relations.

## N-grams for Building Language Models
In [this narrative](narrative_on_n-grams.pdf) about n-grams, I define n-grams and describe how they are used to build a language model, list a few applications where n-grams could be used, describe how probabilities are calculated for unigrams and bigrams, and explain the importance of the source text in building a language model. I also describe the importance of smoothing using a simple approach to smoothing, how language models can be used for text generation and the limitations of such an approach, and how language models can be evaluated. I then introduce the Google Ngram Viewer with an example.

This is a project that consists of 2 Python programs and uses n-grams to build a probabilistic language model from source text. [Program 1](n-grams/program1.py) reads in and processes text from training files written in [English](LangId.train.English), [French](LangId.train.French), and [Italian](LangId.train.Italian). It then creates dictionaries of n-grams for each of the 3 languages using the training data. [Program 2](n-grams/program2.py) uses data from a [test file](LangId.test) to calculate probabilities for each language, for each line in the file. It then compares each probability against true labels from the correct [solution file](LangId.sol) and creates a new file for the predicted solution to display all line numbers from the test file so that each line contains the language with the highest probability for that line. The program also displays the accuracy percentage of language items and the line numbers of incorrectly classified items in the new file.

Program 1 must first be run to get dictionary files of n-grams for each language.

Example command line: *program1.py*

Program 2 can then be run on the terminal by entering the name of the program similarly.