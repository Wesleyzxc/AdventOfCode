# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 17:23:06 2020

@author: Wesley
AoC - Day 5
"""

import math

f = open("data/input5.txt", "r")
inputArray = []
inputArray = [eachLine.strip('\n\r') for eachLine in f]
length = len(inputArray)
#rowLength = len((inputArray[0]))

##### Part 1 #####

def calculateRow(firstSeven):
    rowRange = (0,127)
    for (index, eachBound) in enumerate(firstSeven):
        if (index == len(firstSeven) - 1): # last 
            return rowRange[0] if (eachBound == "F") else rowRange[1]
        rowRange = (rowRange[0], math.floor((rowRange[1]-rowRange[0])/2) + rowRange[0]) if (eachBound == "F") else (math.ceil((rowRange[1]-rowRange[0])/2 + rowRange[0]), rowRange[1])

def calculateColumn(lastThree):
    rowRange = (0,7)
    for (index, eachBound) in enumerate(lastThree):
        if (index == len(lastThree) - 1): # last 
            return rowRange[0] if (eachBound == "L") else rowRange[1]
        rowRange = (rowRange[0], math.floor((rowRange[1]-rowRange[0])/2) + rowRange[0]) if (eachBound == "L") else (math.ceil((rowRange[1]-rowRange[0])/2 + rowRange[0]), rowRange[1])


def main():
    seatID = 0
    idList = []
    for eachID in inputArray:
        row = calculateRow(eachID[0:7])
        column = calculateColumn(eachID[7::])
        newID = (row * 8) + column 
        seatID = newID if (newID > seatID) else seatID # part 1
        idList.append(newID)
    
    print(seatID) # part 1
    
    ##### Part 2 #####
    
    for possibleID in range(min(idList),max(idList)+1):
        if possibleID not in idList:
            print(possibleID)  # part 2
    
if __name__ == "__main__":
    main()