# Assignment 5: N-grams
# Program 1
# This program:
#   - reads in and processes text from training files written in English, French, and Italian
#   - creates bigram and unigram dictionaries for each of the 3 languages using the provided training data
#   - uses the unigram or bigram text as the dictionary key and count of that unigram or bigram in the data as the dictionary value

import os, re, nltk, pickle
from os.path import exists as file_exists
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter

# function that accepts input filename as argument, processes text in the file using n-grams, and returns unigram and bigram dictionaries
def create_ngrams_dict(file):
    # exits program if filename does not match existing file
    if not file_exists(file):
        print("'" + file + "' is not a valid filename.")
        exit(1)
    
    # opens input file and reads it in as raw text
    with open(os.path.join(os.getcwd(), file), 'r', encoding='utf8') as f:
        raw_text = f.read()
    
        # removes newlines
        text = re.sub('\n', ' ', raw_text)
    
        # tokenizes the text
        text = word_tokenize(text)
        
        # uses nltk to create a bigrams list
        bigrams = list(ngrams(text, 2))
        
        # use nltk to create a unigrams list
        unigrams = list(ngrams(text, 1))
        
        # uses the bigrams list to create a bigram dictionary of bigrams and counts, [‘token1 token2’] -> count
        #bigram_dict = {b:bigrams.count(b) for b in set(bigrams)}       # count() method expensive to run
        bigram_dict = dict(Counter(bigrams))
        
        # uses the unigrams list to create a unigram dictionary of unigrams and counts, [‘token’] -> count
        #unigram_dict = {u:unigrams.count(u) for u in set(unigrams)}    # count() method expensive to run
        unigram_dict = dict(Counter(unigrams))
    
    # returns unigram dictionary and bigram dictionary from function
    return unigram_dict, bigram_dict


# main function
def main():
    # calls the above function to process text in English training file and return unigram and bigram dictionaries
    english_unigram_dict, english_bigram_dict = create_ngrams_dict('LangId.train.English')
    # calls the above function to process text in French training file and return unigram and bigram dictionaries
    french_unigram_dict, french_bigram_dict = create_ngrams_dict('LangId.train.French')
    # calls the above function to process text in Italian training file and return unigram and bigram dictionaries
    italian_unigram_dict, italian_bigram_dict = create_ngrams_dict('LangId.train.Italian')
    
    # pickles the 3 unigram and 3 bigram dictionaries and saves to corresponding files using write binary
    pickle.dump(english_unigram_dict, open('english_unigram_dict.p', 'wb'))
    pickle.dump(english_bigram_dict, open('english_bigram_dict.p', 'wb'))
    pickle.dump(french_unigram_dict, open('french_unigram_dict.p', 'wb'))
    pickle.dump(french_bigram_dict, open('french_bigram_dict.p', 'wb'))
    pickle.dump(italian_unigram_dict, open('italian_unigram_dict.p', 'wb'))
    pickle.dump(italian_bigram_dict, open('italian_bigram_dict.p', 'wb'))
    
    # displays notification when program completes saving the 6 dictionaries into files
    print("\nCompleted creating files for unigram and bigram dictionaries in English, French, and Italian")


# calls main function
if __name__ == '__main__':
    main()