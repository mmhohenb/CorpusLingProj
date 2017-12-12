# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:25:05 2017

@author: Mercedes

Goal: pre-proccess text from Project Gutenberg to pull randomized sentences out (and parse them)
"""
import re, random


def preprocess(inputnovel):
    with open(inputnovel) as originalText:
        originalText.readline()
        sansPostText = []
        for line in originalText:
            if "END OF THIS PROJECT GUTENBERG EBOOK" in line:
                break
            else: sansPostText.append(line)
            
        for string in sansPostText:
            if "***" in string:
                sansPostText.pop(0)
                break
            else:
                sansPostText.pop(0)
            
        rStrippedText = []
        for string in sansPostText:
            string.rstrip()
            sansPostText2 = re.sub('\n','',string)
            rStrippedText.append(sansPostText2)
            
        textAsString = ' '.join(rStrippedText)
        preprocessed = re.sub('  ', ' ',textAsString)
        return(preprocessed)
        
'''TO DO: SPLIT NOVEL INTO SENTENCES'''  

def randomsentences():  #Need to input file of text with each individual sentence as one string in a list of all of the strings 
        #count number of sentences (lines)
        sentcount = 500
        rscount = 0
        sentenceNumbers = []
        while rscount <50:
            randomnumber = random.randint(0,sentcount)
            if randomnumber in sentenceNumbers:
                pass
            else:
                sentenceNumbers.append(randomnumber)
                rscount +=1
        return(sentenceNumbers)
    
                
                
WizardOz = "C:/Users/Mercedes/Desktop/L615/ProjectGutenbergInput/pg55.txt"

#print(preprocess(WizardOz))
print(randomsentences())

'''want FOR loop to run each novel through the preprocessing and random sentence pulling
final output will be list of all novels sentences, which will then be sent to a parser'''