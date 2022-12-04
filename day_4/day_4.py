"""
Day 4 of the "Advent of Code"

Link : 
https://adventofcode.com

Author : Eliott
Year : 2022
"""


def fully_pairs(file: list) -> int:
    """
    Count the number of pairs that completely contain the other pair.

    Args:
        file (list): Input

    Returns:
        int: Number of pairs
    """
    count = 0
    for i in file:
        if (i[0] <= i[2] and i[1] >= i[3]) or (i[0] >= i[2] and i[1] <= i[3]):
            count += 1
    return count

def overlapping(file: list) -> int:
    """
    Count the number of overlaps there are

    Args:
        file (list): Input

    Returns:
        int: Number of overlaps
    """
    count = 0
    for i in file:
        if (i[0] >= i[2] and i[0] <= i[3]) or (i[1] >= i[2] and i[1] <= i[3]) or (i[2] >= i[0] and i[2] <= i[1]) or (i[3] >= i[0] and i[3] <= i[1]):
            count += 1
    return count
     

input = []
with open("input.txt") as f:
    for i in f:
        l = i.strip()
        left, right = l.split(',')
        l1, l2 = left.split('-')
        r1, r2 = right.split('-')
        input.append((int(l1), int(l2), int(r1), int(r2))) 

print(fully_pairs(input))
print(overlapping(input))