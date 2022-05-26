import random
from words import wordsList
import string

#function to get a word from the wordlist 

def get_a_word(wordslist):
    hangmanword = random.choice(wordslist)
    while '-' in wordslist ' ' in wordsList:
        handmanword = random.choice(wordsList)
        
    return handmanword 

#function to keep track of words that are guessed and not guessed correctly 
def hangman():
    word = get
