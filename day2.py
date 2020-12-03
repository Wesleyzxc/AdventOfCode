# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:48:06 2020

@author: Wesley
AoC - Day 2
"""

import re

f = open("data/input2.txt", "r")
inputArray = []
inputArray = [eachLine.strip('\n\r') for eachLine in f]
length = len(inputArray)

##### Part 1 #####

def splitRow(row):
    requirement = re.search("([0-9]+)-([0-9]+) ([a-z]): ([a-z]*)", row)
    lowerBound = int(requirement.group(1))
    upperBound = int(requirement.group(2))
    if (lowerBound > upperBound):
        storedValue = lowerBound
        lowerBound = upperBound
        upperBound = storedValue
    character = requirement.group(3)
    password = requirement.group(4)
    #password = requirement[1]
    return({"lowerBound": lowerBound, "upperBound": upperBound, "character": character, "password": password})

def checkPasswordCount(dataDict):
    password = dataDict["password"]
    character = dataDict["character"]
    lowerBound = dataDict["lowerBound"]
    upperBound = dataDict["upperBound"]
    if (password.count(character) >= lowerBound and password.count(character) <= upperBound):
        return True
    else:
        return False



##### Part 2 #####
    
def checkPasswordPosition(dataDict):
    password = dataDict["password"]
    character = dataDict["character"]
    lowerBound = dataDict["lowerBound"]
    upperBound = dataDict["upperBound"]
    if (password[lowerBound-1] == character and password[upperBound-1] != character):
        return True
    elif (password[lowerBound-1] != character and password[upperBound-1] == character):
        return True
    else:
        return False



def checkList(array):
    validPasswordsCount = 0
    validPasswordsPosition = 0
    for eachIndex in range(length):
        data = splitRow(inputArray[eachIndex])
        if checkPasswordCount(data):
            validPasswordsCount = validPasswordsCount + 1
        if checkPasswordPosition(data):
            validPasswordsPosition = validPasswordsPosition + 1
    return (validPasswordsCount, validPasswordsPosition)


if __name__ == "__main__":
    print(checkList(inputArray))