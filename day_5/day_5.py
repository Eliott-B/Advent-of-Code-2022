"""
Day 5 of the "Advent of Code"

Link : 
https://adventofcode.com

Author : Eliott
Year : 2022
"""

def open_file(link) -> list:
    """
    Transform the input.txt to few list

    Args:
        link (): Link of the document

    Returns:
        list: Lists.
    """
    f = open(link)
    string  = f.read().split('\n')
    results = [list(map(str,s.strip().split(' '))) for s in string]
    for i in range(10):
        results.pop(0)
    results.pop()
    remove_str(results)
    return results

def open_file2(link) -> list:
    """
    Transform the input.txt to few list

    Args:
        link (): Link of the document

    Returns:
        list: Lists.
    """
    stacks = {}
    for i in range(1, 10):
        stacks[i] = []
    with open(link) as f:
        for line in f.readlines():
            if not (line.startswith("move")):
                for i in range(1, len(line),4):
                    if line[i] != ' ':
                        stacks[i//4+1].append(line[i])
    for i in range(1,len(stacks)+1):
        stacks[i].reverse()
    for i in stacks.keys():
        stacks[i].pop(0)
    return stacks

def remove_str(str_list: list) -> list:
    """
    Remove string in the list

    Args:
        str_list (list): start list

    Returns:
        list: end list
    """
    for i in str_list:
        for j in i:
            if type(j) == str:
                i.remove(j)
        for k in range(len(i)):
            i[k] = int(i[k])

def orga(pile,ordre):
    for i in ordre:
        for j in range(i[0]):
            k = pile[i[1]].pop(-1)
            pile[i[2]].append(k)
    return pile

def orga2(pile,ordre):
    for i in ordre:
        for j in range(i[0],0,-1):
            k = pile[i[1]].pop(-j)
            pile[i[2]].append(k)
    return pile

def last(pile):
    r = ''
    for i in pile.keys():
        r += pile[i][-1]
    return r

input = open_file('day_5/input.txt')
input2 = open_file2('day_5/input.txt')
orga(input2,input)
print(last(input2))
input3 = open_file2('day_5/input.txt')
orga2(input3,input)
print(last(input3))