# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:31:59 2017

@author: Mercedes
"""
import nltk


def example(inputfile):
    wordlist = []
    with open(inputfile) as f:
        view = f.readlines()
        wtokenized = nltk.word_tokenize(view)
        for word in wtokenized:
            wordlist.append(word)
        return(wordlist)

print(example("C:/Users/Mercedes/Desktop/SANTA/03_Anderson.txt"))      