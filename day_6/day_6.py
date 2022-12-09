"""
Day 6 of the "Advent of Code"

Link : 
https://adventofcode.com

Author : Eliott
Year : 2022
"""

def find(input):
    for i in range(len(input)-5):
        tmp = [input[i+j] for j in range(4)]
        test = True
        for k in tmp:
            if tmp.count(k) > 1:
                test = False
                break
        if test == True:
            return i+4

def find2(input):
    for i in range(len(input)-15):
        tmp = [input[i+j] for j in range(14)]
        test = True
        for k in tmp:
            if tmp.count(k) > 1:
                test = False
                break
        if test == True:
            return i+14

f = open('day_6/input.txt')
input  = f.read()
print(find(input))
print(find2(input))