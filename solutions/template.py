import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def read_input():
    with open("inputs/day00.txt", "r") as f: # CHANGE HERE <--
        lines = f.readlines()
    return [line.strip('\n') for line in lines]
    
def solve_part1(datas):
    pass

def solve_part2(datas):
    pass

if __name__ == "__main__":
    if not os.path.isfile("inputs/day00.txt"): # CHANGE HERE <--
        fetch(0)  # CHANGE HERE <--
    else:
        print("Input file already exists.")
    
    datas = read_input()
    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))