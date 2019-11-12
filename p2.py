# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:35:49 2019

@author: Samsung
"""

def getGuessedWord(secretWord,lettersGuessed):
    word = ""
    for char in secretWord:
        if char in lettersGuessed:
            word = word + char
        else: 
            word = word + "_"
    return word
        
        