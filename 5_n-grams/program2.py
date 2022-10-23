# Assignment 5: N-grams
# Program 2
# This program:
#   - uses test data from the file 'LangId.test' to calculate probabilities for each language, for each line in the file
#   - compares each probability against true labels from the solution file 'LangId.sol'
#   - displays each line number from the test file next to the language with the highest probability for that line in a new file called 'guessed_solution.txt'
#   - outputs the accuracy of language items as a percentage of correctly classified instances in the test set based on the guessed count
#   - outputs the line numbers of incorrectly classified items

import nltk, pickle
from nltk import word_tokenize
from nltk.util import ngrams

# main function
def main():
    # reads in the 6 pickled dictionaries using read binary
    english_unigram_dict_in = pickle.load(open('english_unigram_dict.p', 'rb'))
    english_bigram_dict_in = pickle.load(open('english_bigram_dict.p', 'rb'))
    french_unigram_dict_in = pickle.load(open('french_unigram_dict.p', 'rb'))
    french_bigram_dict_in = pickle.load(open('french_bigram_dict.p', 'rb'))
    italian_unigram_dict_in = pickle.load(open('italian_unigram_dict.p', 'rb'))
    italian_bigram_dict_in = pickle.load(open('italian_bigram_dict.p', 'rb'))
    
    # creates file to store guessed solution for comparison with correct solution
    with open('guessed_solution.txt', 'w') as f:
        f.close()
    
    # opens the test file and reads in the lines of text into list of strings
    with open('LangId.test', 'r') as f:
        test_file = f.readlines()

    # opens the correct solution file and reads in the lines of text into list of strings
    with open('LangId.sol', 'r') as f:
        solution_file = f.readlines()

    # gets variable v as the total vocabulary size by adding the lengths of the 3 unigram dictionaries
    v = len(english_unigram_dict_in) + len(french_unigram_dict_in) + len(italian_unigram_dict_in)

    # initializes counters
    line_number = 0
    correct_items_count = 0

    # loops through each line in test file to compare probabilities between languages
    for text in test_file:
        line_number += 1

        english_probability = compute_probability(text, english_unigram_dict_in, english_bigram_dict_in, v)
        french_probability = compute_probability(text, french_unigram_dict_in, french_bigram_dict_in, v)
        italian_probability = compute_probability(text, italian_unigram_dict_in, italian_bigram_dict_in, v)

        # writes the language with the highest probability to the guessed solution file
        if english_probability > italian_probability and english_probability > french_probability:
            with open('guessed_solution.txt', 'a') as f:
                f.write(str(line_number))
                f.write(" English\n")
        elif italian_probability > english_probability and italian_probability > french_probability:
            with open('guessed_solution.txt', 'a') as f:
                f.write(str(line_number))
                f.write(" Italian\n")
        else:
            with open('guessed_solution.txt', 'a') as f:
                f.write(str(line_number))
                f.write(" French\n")

    # opens the guessed solution file and reads in the lines of text into list of strings
    with open('guessed_solution.txt', 'r') as f:
        guessed_solution = f.readlines()

    # gets count of lines from guessed solution file by calculating length
    guessed_count = len(guessed_solution)
    
    # stores line numbers of incorrect language items into list
    incorrect_items = []
    
    # compares correct solution in file 'LangId.sol' to guessed solution in file 'guessed_solution.txt'
    for i in range(guessed_count):
        if guessed_solution[i] == solution_file[i]:
            correct_items_count += 1
        else:
            incorrect_items.append(i + 1)
    
    # displays the accuracy of language items (as the percentage of correctly classified instances in the test set based on the guessed count)
    accuracy = (correct_items_count / guessed_count) * 100
    print("\nAccuracy of tested language: %.2f" % accuracy + "%")
    # displays the line numbers of the incorrectly classified language items
    print("Line numbers of incorrect items:", incorrect_items)


# function that calculates a probability for each language, for each line of text in the test file
def compute_probability(text, unigram_dict, bigram_dict, v):
    p_laplace = 1                                                           # calculates probability p using Laplace smoothing
    unigrams = word_tokenize(text)
    bigrams = list(ngrams(unigrams, 2))
    
    for bigram in bigrams:
        b = bigram_dict[bigram] if bigram in bigram_dict else 0             # gets variable b as the bigram count
        u = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0     # gets variable u as the unigram count of the first word in the bigram
        p_laplace = p_laplace * ((b + 1) / (u + v))
        
    return p_laplace


# calls main function
if __name__ == '__main__':
    main()