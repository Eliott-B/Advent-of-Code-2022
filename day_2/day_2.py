"""
Second day of the "Advent of Code"

Link : 
https://adventofcode.com

Author : Eliott
Year : 2022
"""
POINT = [['A','X',3], ['A','Y',6], ['A','Z',0], ['B','X',0], ['B','Y',3], ['B','Z',6], ['C','X',6], ['C','Y',0], ['C','Z',3]]
BONUS = [["X",1], ["Y",2], ["Z",3]]
GAGNE = [["X",0], ["Y",3], ["Z",6]]
JOUEUR1 = ['A','B','C']
JOUEUR2 = ['X','Y','Z']


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
    list_str = [list(map(str,s.strip().split(' '))) for s in string]
    return list_str

def point(game: list) -> int:
    """
    Count the point of the game

    Args:
        game (list): Game list

    Returns:
        int: Points resultes
    """
    total = 0
    for i in game:
        for j in POINT:
            if i == [j[0],j[1]]:
                total += j[2]
        for k in BONUS:
            if i[1] == k[0]:
                total += k[1]
    return total

def strat2(game: list) -> int:
    """
    Count the point of the game with the strategy of the elf

    Args:
        game (list): Game list

    Returns:
        int: Points resultes
    """
    total = 0
    for i in game:
        if i[1] == 'X':
            total += GAGNE[0][1]
            j = JOUEUR1.index(i[0])
            total += BONUS[j-1][1]
        elif i[1] == 'Y':
            total += GAGNE[1][1]
            j = JOUEUR1.index(i[0])
            total += BONUS[j][1]
        elif i[1] == 'Z':
            total += GAGNE[2][1]
            j = JOUEUR1.index(i[0])
            total += BONUS[(j+1)%3][1]
    return total
        

file = open_file("input.txt")
file.pop()
print(point(file))
print(strat2(file))