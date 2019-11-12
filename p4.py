# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:57:34 2019

@author: Samsung
"""

from p1 import isWordGuessed 

from p2 import getGuessedWord

from p3 import getAvailableLetters

def Hangaroo(secretWord):
    print("Welcome, the fate of the kangaroo depends on you!")
    print("Your secret word contains " + str(len(secretWord)) + " letters.")
    lettersGuessed = ''
    guessesLeft = 5
    print("----------------")
    while True: 
        print("You have " + str(guessesLeft) + " guesses left.")
        print("You still have these available letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Guess a letter: ")
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed = lettersGuessed + guess 
            print(getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
            print("You have already guessed that letter. Try again " + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed = lettersGuessed + guess
            print("That letter is not in the word. Try again " + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft = guessesLeft - 1
        print("--------------")
        if guessesLeft <= 0:
            print("Oops! You have ran out of guesses. The secret word was " + secretWord + ".")
            break
        if isWordGuessed(secretWord,lettersGuessed):
            print("You have won!")
            break
        
        