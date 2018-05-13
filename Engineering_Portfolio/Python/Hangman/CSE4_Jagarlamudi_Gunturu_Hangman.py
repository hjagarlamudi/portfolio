from __future__ import print_function
import random

# Day1: We began the function but we didn't really get anywhere with it

# Day2: We started over the function and with some deep thinking, we found
# an algorithm that may work for the function and after trying it out a bunch
# of times, we finally got it. 

# Day3: Made a working college themed hangman game. Added a list of colleges.

# Day4: Commented EVERYTHING and added a the possibility of losing to the game

#predefined variables
words = ['']
guess_incorrect = [5]

#Hangman ASCII art list
hangman_art = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def h_d(guessed, secret):
    '''function that checks if certain letters are in the secret message'''
    
    #empty message string that is rewritten to show player's progress
    message = ''
    
    #checks the number of incorrect guesses
    if 1 == 1:
        guess_incorrect[0] = 6
        for i in guessed:
            if i not in secret:
                guess_incorrect[0] -= 1
    
    #for loop that checks conditions for every letter in the secret
    for i in secret: 
        #reveals the letter if it is in the secret and guessed letters list
        if i in guessed: 
            message += i
        
        #puts spaces in the secret message where they should be
        elif i == ' ': 
            message += ' '
        
        #conceals letters in secret if they are not in the guessed letters list
        else: 
            message += '-' 
    
    #shows the player the concealed secret
    print(message)
    
    #ASCII artwork for hangman
    
    # Empty noose if no incorrect guesses
    if guess_incorrect[0] == 6:
        print(hangman_art[0])
    
    # Noose with head if one incorrect guess
    elif guess_incorrect[0] == 5:
        print(hangman_art[1])
    
    #Noose with head and body if two incorrect guesses
    elif guess_incorrect[0] == 4:
        print(hangman_art[2])
    
    #Noose with head, body, and one arm if three incorrect guesses
    elif guess_incorrect[0] == 3:
        print(hangman_art[3])
    
    #Noose with head, body, and two arms if four incorrect guesses
    elif guess_incorrect[0] == 2:
        print(hangman_art[4])
    
    #Noose with head, body, two arms and one leg if five incorrect guesses
    elif guess_incorrect[0] == 1:
        print(hangman_art[5])
   
   #Noose with full body if six incorrect guesses (you lose)
    else:
        print(hangman_art[6])
        
    
    #stores the correct answer for the while loop's conditional
    if message == secret:
        words[0] = message
    
def hangman(): 
    '''hangman college edition game'''
    
    # list of colleges the game can choose from
    secret_list = ['yale', 'uc berkeley', 'las positas', 'diablo valley college'
    , 'stanford', 'purdue', 'carnegie mellon', 'harvard', 'dartmouth',
    'princeton', 'california institute of technology', 'cornell', 'brown',
    'massachusetts institute of technology','university of pennsylvania',
    'case western', 'uc los angeles', 'uc irvine', 'uc san diego'
    , 'uc riverside', 'oxford', 'cambridge', 'john hopkins', 'duke', 
    'university of munich', 'vanderbilt', 'northwestern', 'emory university',
    'university of michigan ann arbor', 'georgia institute of technology',
    'pepperdine', 'syracuse', 'virginia tech', 'rice university', 'georgetown',
    'college of wooster', 'columbia', 'new york university', 
    'university of north carolina chapel hill', 'india institute of technology', 
    'fiji institute of technology', 'victoria university',
    'beijing institute of technology', 'middle east college',
    'defiance college', 'national american university',
    'univeristy of southern california',
    'slippery rock university of pennsylvania']
    
    # list that is checked to see what you have already guessed.
    guessed = []
    
    # picks a random college for the player to guess
    secret = random.choice(secret_list)
    
    #Game Introduction
    print('Welcome to our hangman game (college edition). Guess the college',
    'name!')
    
    #while loop that checks if the secret is unveiled
    while words[0] != secret:
        
        #ends function if you incorrectly guess too much
        if guess_incorrect[0] == 0:
            break
        
        #looping guess
        guess = raw_input('Guess one lowercase letter: ')
        
        #checks to see if player input full correct answer
        if guess == secret:
            words[0] = secret
        
        #checks to see if player already guess something
        elif guess in guessed: 
            print('You already guessed that!')
        
        #redirects to the h_d function and adds thh guess to the list of inputs
        else: 
            guessed.append(guess)
            h_d(guessed, secret)
    
    #clears guess values
    del guessed[:]
    
    #Lose: guess wrong too much, Win: guess correctly
    if guess_incorrect[0] == 0:
        print('You guess incorrectly too much. You lose!')
        
        #prints answer for the loser to see
        print('The answer is', secret, '.')
        
        #resets values in list
        guess_incorrect[0] = 6
        words[0] = ''
    else:
        print('You win!')
        
        #resets values in list
        guess_incorrect[0] = 6
        words[0] = ''