# Assignment 3: Word Guessing Game
# This program:
#   - reads in an input text file (anat19.txt)
#   - preprocesses the text in the file to display lexical diversity, 20 POS tags, number of tokens, number of noun lemmas, and 50 most common words from the file
#   - randomly chooses a word from a list of the top 50 words in the preprocessed text
#   - simulates a word guessing game using the random word

import sys, os, random, nltk
from os.path import exists as file_exists
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# main function
def main():
    # if sys arg does not include input filename, prints error message and exits program
    if len(sys.argv) < 2:
        print("Please enter the name of the input file as a system argument.")
        exit(1)

    # sends filename to main program in a system argument
    file = sys.argv[1]
    
    # exits program if filename specified in system argument does not match existing file
    if not file_exists(file):
            print("'" + file + "' is not a valid filename.")
            exit(1)
    
    # opens input file for reading
    with open(os.path.join(os.getcwd(), file), 'r') as f:
        # reads in input file as raw text
        text = f.read()
        
    # calculates and displays lexical diversity of tokenized raw text
    tokens = word_tokenize(text)
    unique_tokens = set(tokens)
    print("\nLexical diversity: %.2f" % (len(unique_tokens) / len(tokens)))
    
    # calls function to preprocess input file text 
    tokens, noun_lemmas = preprocess_text(text)
    # creates list to store 50 common words to guess from
    common_words = []
        
    # makes dictionary of {noun:count of noun in tokens} items from the nouns and tokens lists
    counts = {t:tokens.count(t) for t in noun_lemmas}

    # sorts the dictionary by count
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    # loops through dictionary and prints the 50 most common words and their counts
    print("\n50 most common words:")
    for i in range(50):
        # saves the 50 most common words to a list for use in guessing game
        common_words.append(sorted_counts[i])
        print(sorted_counts[i])

    # calls function to simulate word guessing game using the list of 50 common words from input file
    guessing_game(common_words)


# function that preprocesses raw text from input file
def preprocess_text(text):
    # converts raw text into lowercase
    text = text.lower()
    # tokenizes lowercase text
    tokens = word_tokenize(text)
    # reduces tokens to only those that are alpha, not in the NLTK stopword list, and have length > 5
    tokens = [t for t in tokens if t.isalpha() and t not in stopwords.words('english') and len(t) > 5]
    
    # lemmatizes tokens
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]
    # makes a list of unique lemmas from lemmatized tokens
    unique_lemmas = list(set(lemmas))
    
    # does POS tagging on the unique lemmas
    tags = pos_tag(unique_lemmas)
    # prints the first 20 tagged items
    print("\nFirst 20 tagged items:", tags[:20])
    
    # creates list of only those lemmas that are nouns
    noun_lemmas = list([t[0] for t in tags if t[1].startswith('N')])
    
    # prints the number of tokens
    print("\nNumber of tokens:", len(tokens))
    # prints the number of lemmas that are nouns
    print("\nNumber of nouns:", len(noun_lemmas))
    
    # returns tokens and noun lemmas
    return tokens, noun_lemmas


# function that simulates a word guessing game using common 50 words from input file
def guessing_game(common_words):
    # keeps a cumulative total score, giving user 5 points to start game with
    score = 5
    
    # randomly chooses 1 of 50 words in the top 50 list
    word_to_guess = random.choice(common_words)[0]
    
    # stores correct letters of randomly chosen word and all letters from user guesses into lists
    word_letters = []
    guessed_letters = []

    print("\n\nLet's play a word guessing game! Enter '!' to exit the game at any time.\n\nYour initial score is", score, "\n")
    
    # outputs to console an underscore space for each letter in the randomly chosen word
    print("Word: ", end = "")
    for letter in word_to_guess:
        print("_", end = " ")
    
    # loops through randomly chosen word and gets letter guesses from user while total user score is positive
    while score > -1:
        # asks user to guess a letter
        guess = input('\n\nGuess a letter: ')
        # converts input letter into lowercase
        guess = guess.lower()
        
        # ends game if user guesses '!'
        if guess == "!":
            print("\nExiting game...")
            exit(0)
        # checks if user input for each guess is a letter
        elif guess.isalpha() == False:
            print("\nYou can only guess letters. Try again.", end = "")
        # checks if letter was already entered previously 
        elif guess in guessed_letters:
            print("\nYou already guessed the letter '" + guess + "'. Try again.", end = "")
        else:
            # add and store all letter guesses into list
            guessed_letters.append(guess)    
            # if the letter is in the word, fills in all matching letter _ with the letter and adds 1 point to user score
            if guess in word_to_guess:
                score += 1
                # add and store only correct letters of word into list
                word_letters.append(guess)
                # gives user feedback on their score for the word after each guess
                print("\nRight! Your score is", score, "\n")
            # if the letter is not in the word, subtracts 1 from user score
            else:
                score -= 1
                # ends game when total user score is negative
                if score == -1:
                    print("\nSorry, you lost! The word was \"" + word_to_guess + "\".\nYour current score is", score)
                    print("\nExiting game...")
                    exit(1)
                # give user feedback on their score for the word after each guess
                else:
                    print("\nSorry, guess again. Your score is ", score, "\n")

            # counts number of correct guesses and displays word content after each guess
            correct_guesses = 0
            print("Word: ", end = "")
            for letter in word_to_guess:
                if letter in word_letters:
                    print(letter, end = " ")
                    correct_guesses += 1
                else:
                    print('_', end = " ")
            # ends game if user guesses the right word
            if correct_guesses == len(word_to_guess):
                print("\n\nYou solved it!\nYour current score is", score)
                print("\nExiting game...")
                exit(0)


# calls main function
if __name__ == '__main__':
    main()