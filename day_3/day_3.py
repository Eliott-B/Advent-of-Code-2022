"""
Day 3 of the "Advent of Code"

Link : 
https://adventofcode.com

Author : Eliott
Year : 2022
"""

a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
A = [x.upper() for x in a]
PRIO = a+A


def open_file(link: str) -> list:
    """
    Transform the input.txt to few list

    Args:
        link (str): Link of the document

    Returns:
        list: Lists of the document.
    """
    f = open(link)
    string  = f.read().split('\n')
    return string

def double_character(input: list) -> list:
    """
    Give the character that is duplicated.

    Args:
        input (list): List input

    Returns:
        list: Duplicated character
    """
    output = []
    for i in input:
        x = i[:len(i)//2]
        y = i[len(i)//2 if len(i)%2 == 0 else (((len(i)//2))+1):]
        j,end = 0,False
        while end != True and j != len(y):
            if y[j] in x:
                output.append(y[j])
                end = True
            j += 1
    return output

def count_prio(character: list) -> int:
    """
    Counts the priority points of the characters.

    Args:
        character (list): Character list

    Returns:
        int: Priority points
    """
    point = 0
    for i in character:
        point += PRIO.index(i)+1
    return point

def part2(chara: list) -> list:
    """
    Give the character that is duplicated on 3 lines.

    Args:
        chara (list): List input

    Returns:
        list: Duplicated character
    """
    output = []
    for i in range(0,len(chara)-1,3):
        x,y,z = chara[i],chara[i+1],chara[i+2]
        j,end = 0,False
        while end != True and j != len(x):
            if x[j] in y and x[j] in z:
                output.append(x[j])
                end = True
            j += 1
    return output


file = open_file("input.txt")
file.pop()
chara = double_character(file)
print(count_prio(chara))
chara2 = part2(file)
print(count_prio(chara2))