"""
First day of the "Avent of Code"

Link : 
https://adventofcode.com

Author : Eliott
Year : 2022
"""

def get_calories(link) -> list:
    """
    Transform the input.txt to few list

    Args:
        link (): Link of the document

    Returns:
        list: Lists for differents elfs.
    """
    f = open(link)
    string  = f.read().split('\n\n')
    calories_list = [list(map(int,s.strip().split('\n'))) for s in string]
    return calories_list

def count_calories(calories: list) -> list:
    """
    Count the number of calories for elfs.

    Args:
        calories (list): Number of calories.
   
    Returns:
        list: List of calories
    """
    calories_list = []
    for i in range(len(calories)):
        calories_list.append(0)
        for j in range(len(calories[i])):
            calories_list[i] += calories[i][j]
    return calories_list

def find_max(cal: list) -> int:
    """
    Find the max calories in the list.

    Args:
        cal (list): Calories list

    Returns:
        int: Calories max
    """
    max = 0
    for i in cal:
        if i > max:
            max = i
    return max

def sum_3(cal:list) -> int:
    """
    Find the calories of the top three.

    Args:
        cal (list): Calories list

    Returns:
        int: Calories of the top three
    """
    cal2 = cal
    cal2.sort(reverse=True)
    top3 = cal2[0] + cal2[1] + cal2[2]
    return top3
        

cal_list = get_calories("input.txt")
elfs = count_calories(cal_list)
print("Le max est",find_max(elfs))
print("Le top 3 est",sum_3(elfs))