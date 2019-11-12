# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 19:48:02 2019

@author: Samsung
"""

def getAvailableLetters(lettersGuessed):
    letters = "abcdefghijklmnopqrstuvwxyz"
    string = ""
    for char in letters:
        if char not in lettersGuessed:
            string = string + char
    return string