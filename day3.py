# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:48:06 2020

@author: Wesley
AoC - Day 3
"""

f = open("data/input3.txt", "r")
inputArray = []
inputArray = [eachLine.strip('\n\r') for eachLine in f]
length = len(inputArray)
rowLength = len((inputArray[0]))

##### Part 1 #####

def nextPosition(position, nextRow, nextIndex):
    row = position[0] + nextRow
    index = (position[1] + nextIndex) % rowLength
    return (row,index)

def checkTree(position):
    if (inputArray[position[0]][position[1]] == '#'):
        return True
    else:
        return False
    
##### Part 2 #####

def getTrees(downNo, rightNo):
    numTree = 0;
    position = (0,0)
    while (position[0] < length):
        if checkTree(position):
            numTree = numTree + 1
        position = nextPosition(position, downNo, rightNo)
    return numTree

def main():
    slope_1 = getTrees(1,1)
    slope_2 = getTrees(1,3)
    slope_3 = getTrees(1,5)
    slope_4 = getTrees(1,7)
    slope_5 = getTrees(2,1)
    print(slope_1 * slope_2 * slope_3 * slope_4 * slope_5 )
    
if __name__ == "__main__":
    main()