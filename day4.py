# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 08:48:06 2020

@author: Wesley
AoC - Day 4
"""

import re

f = open("data/input4.txt", "r")
inputArray = f.read()[:-1].split('\n\n')
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eyeColour = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

###### Part 1 #####
  
def checkUsers():
    validUsers = 0
    for users in inputArray:
        fields = re.split('[\n ]', users)
        pairing = dict(field.split(':') for field in fields)
        if all(key in pairing for key in keys):
            validUsers += 1
    return validUsers
  
print(checkUsers())

###### Part 2 #####


def checkUsersPart2():
    validUsers = 0
    for users in inputArray:
        fields = re.split('[\n ]', users)
        pairing = dict(field.split(':') for field in fields)
        if all(key in pairing for key in keys):
            if 1920 <= int(pairing['byr']) <= 2002\
                and 2010 <= int(pairing['iyr']) <= 2020\
                and 2020 <= int(pairing['eyr']) <= 2030\
                and re.match(r'\d+..', pairing['hgt'])\
                and (pairing['hgt'].endswith('cm') and 150 <= int(pairing['hgt'][:-2]) <= 193 or pairing['hgt'].endswith('in') and 59 <= int(pairing['hgt'][:-2]) <= 76)\
                and re.match(r'^#[\da-f]{6}$', pairing['hcl'])\
                and pairing['ecl'] in eyeColour\
                and re.match(r'^\d{9}$', pairing['pid']):
                validUsers += 1
    return validUsers

print(checkUsersPart2())