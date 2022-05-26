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
    while len(letters_in_word) > 0:
    #what letters has the user used 
    # ' '.join(['a', 'b', 'cd']) --> 'a,b,cd'
         print('you have used the following letters: ',' '.joined(letters_used))
    
    #what is the current word they are guessing(ex: l _ V _)
         wordsList = [letter if letter in user_letter else '-' for letter in wordsList]
         print('The current word: ',' '.join(wordsList))
    
         user_letter = input('Guess a Letter: ').upper()
         if user_letter in alphabet - letters_used: 
             user_letter.add(user_letter)
             if user_letter in letters_in_word:
                 letters_in_word.remove(user_letter)
        
        elif user_letter in letters_used:
            print('You have already guessed this letter, try again. ')
        else:
        print('Invalid character entered. Please Try Again')

#