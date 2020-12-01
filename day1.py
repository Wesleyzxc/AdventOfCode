# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:48:06 2020

@author: Wesley
AoC - Day 1
"""

f = open("data/input.txt", "r")
inputArray = []
inputArray = [int(eachLine.strip('\n\r')) for eachLine in f]
length = len(inputArray)

##### Part 1 #####

def get2Index(length):
    for eachIndex in range(length):
        nextIndex = eachIndex + 1
        for (nextIndex) in range(length):
            if (inputArray[eachIndex] + inputArray[nextIndex]) == 2020:
                return(inputArray[eachIndex] * inputArray[nextIndex])
                
answer = get2Index(length)
print(answer)

##### Part 2 #####

def get3Index(length):
    for eachIndex in range(length):
        nextIndex = eachIndex + 1
        for (nextIndex) in range(length):
            lastIndex = nextIndex + 1
            for (lastIndex) in range(length):
                if (inputArray[eachIndex] + inputArray[nextIndex] + inputArray[lastIndex]) == 2020:
                    return(inputArray[eachIndex] * inputArray[nextIndex] * inputArray[lastIndex])

answer = get3Index(length)
print(answer)