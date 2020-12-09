# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 13:52:44 2020

@author: Wesley
AoC - Day 6
"""

import math

f = open("data/input6.txt", "r")
inputArray = f.read()[:-1].split('\n\n')
length = len(inputArray)
#rowLength = len((inputArray[0]))

##### Part 1 #####

def calculateQuestions(group, checked):
    combinedQuestions = group.replace('\n','') 
    for character in combinedQuestions:
        if (character not in checked):
            checked.append(character)
    return len(checked), checked

##### Part 2 #####
    

def calculateEveryone(group):
    combinedQuestions = group.split('\n')
    intersect = combinedQuestions[0]
    for eachLine in combinedQuestions[1::]:
        intersect = set(intersect).intersection(eachLine)
    return len(intersect)

    
def main():
    score = 0
    for eachGroup in inputArray:
        #newScore, checked = calculateQuestions(eachGroup, checked) # part 1
        #score += newScore
        score += calculateEveryone(eachGroup)
    print(score)
    
if __name__ == "__main__":
    main()