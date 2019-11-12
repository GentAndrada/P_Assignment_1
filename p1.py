# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def isWordGuessed(secretWord,lettersGuessed):
    list(secretWord)
    if all(char in lettersGuessed for char in secretWord):
        return True
    else: 
        return False
        