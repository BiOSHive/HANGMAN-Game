import random
from words import wordsList
import string

#function to get a word from the wordlist 

def get_a_word(wordslist):
    hangmanword = random.choice(wordslist)
    while '-' in wordslist or ' ' in wordsList:
        handmanword = random.choice(wordsList)
        
    return handmanword 

#function to keep track of words that are guessed and not guessed correctly 
def hangman():
    word = get_a_word(wordslist)
    letters_in_word = set(wordsList) #will define letters in the word 
    alphabet = set(string.ascii_uppercase)
    letters_used = set() #letters already guessed by user
    
#user input 
user_letter = input('Guess a Letter: ').upper()
if user_letter in alphabet - letters_used: 
    user_letter.add(user_letter)
    if user_letter in letters_in_word:
        letters_in_word.remove(user_letter)
        
elif user_letter in letters_in
