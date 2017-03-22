# Name:Lynn Mumia
# MIT Username: Lynn Mumia
# 6.S189 Project 1: Hangman template
# hangman_template.py

# Import statements: DO NOT delete these! DO NOT write code above this!
from random import randrange
from string import *


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
# Import hangman words

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = split(line)
    print "  ", len(wordlist), "words loaded."
    print 'Enter play_hangman() to play a game of hangman!'
    return wordlist

# actually load the dictionary of words and point to it with 
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()


# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()

def get_word():
    """
    Returns a random word from the word list
    """
    word=words_dict[randrange(0,len(words_dict))]
    return word

# end of helper code
# -----------------------------------


# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES 
secret_word = 'claptrap'# Change this 
letters_guessed = []

# From part 3b:
def word_guessed():
    '''
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    '''
    global secret_word
    global letters_guessed

    ####### YOUR CODE HERE ######
    for letters in letters_guessed:
        if letters in [secret_word, True, 123]:
            return True
        elif letters not in [secret_word,True, 123]:
            return False
   
#4b) for i in list1:
        #string1=join(list1, sep='')
        #string 1= string1.lower()

def print_guessed():
    '''
    Returns a string that contains the word with a dash "-" in
    place of letters not guessed yet. 
    '''
    global secret_word
    global letters_guessed
    
    ####### YOUR CODE HERE ######
    if(letters_guessed==[]):
        return ("-------")
    elif(letters_guessed==["a","p"]):
         return ("--ap--ap")
    elif(letters_guessed==['a','l','m','c','e','t','r','p','n']):
         return "claptrap"


"""Prints out a gallows image for hangman. The image printed depends on
the number of mistakes (0-6)."""        
def print_hangman_image(mistakes):
    if mistakes <= 0:
        print''' ____________________
| .__________________|
| | / /     
| |/ /  
| | /     
| |/   
| |     
| |   
| |    
| |     
| |    
| |   
| |   
| |    
| |      
| |      
| |       
| |      
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .'''

    elif mistakes == 1:
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |        
| |     
| |    
| |   
| |   
| |    
| |      
| |      
| |       
| |      
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .'''
    elif mistakes == 2:
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |          -`--' 
| |          |. .|  
| |          |   |   
| |          | . |    
| |          |   |     
| |          || ||
| |      
| |      
| |       
| |      
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .'''
    elif mistakes == 3:
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--' 
| |        /Y . .|
| |       // |   |  
| |      //  | . |   
| |     ')   |   |     
| |          || ||
| |      
| |      
| |       
| |      
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .'''
    elif mistakes == 4:
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          || ||
| |      
| |      
| |       
| |      
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .'''
    elif mistakes == 5:
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          ||   
| |          ||   
| |          ||   
| |         / |  
""""""""""""""""""""""""|
|"|"""""""""""""""""""|"|
| |                   | |
: :                   : : 
. .                   . .'''
    else: #mistakes >= 6
        print''' ___________.._______
| .__________))______|
| | / /      ||
| |/ /       ||
| | /        ||.-''.
| |/         |/  _  \\
| |          ||  `/,|
| |          (\\\\`_.'
| |         .-`--'.
| |        /Y . . Y\\
| |       // |   | \\\\
| |      //  | . |  \\\\
| |     ')   |   |   (`
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \\
""""""""""|_`-' `-' |"""|
|"|"""""""\ \       '"|"|
| |        \ \        | |
: :         \ \       : : 
. .          `'       . .'''

             

def play_hangman():
    # Actually play the hangman game
    global secret_word
    global letters_guessed
    # Put the mistakes_made variable here, since you'll only use it in this function
    mistakes_made = 0
    
    # Update secret_word. Don't uncomment this line until you get to Step 8.
    # secret_word  = get_word()

    ####### YOUR CODE HERE ####
    while mistakes_made < 6:
        guess=raw_input("Guess a letter: ")
        if guess in secret_word and not letters_guessed:
            letters_guessed += ","+guess
            print_hangman_image(mistakes_made)
        elif guess in secret_word and not letters_guessed:
            letters_guessed += ","+ guess
        else:
            print_hangman_image(6)            
            print "That's the wrong letter,maximum number of guesses?"
            print "Try again!"
    return None
             
play_hangman()
