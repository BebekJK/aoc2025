import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def read_input():
    with open("inputs/day01.txt", "r") as f:
        lines = f.readlines()
    return [line.strip('\n') for line in lines]
    
def solve_part1(datas):
    start, count = 50, 0
    for data in datas:
        direction, dist = data[0], int(data[1:])
        if direction == 'L':
            start = (start - dist + 100) % 100
        else:
            start = (start + dist) % 100
        
        if start == 0:
            count += 1
            
    return count

def solve_part2(datas):
    start, count = 50, 0
    for data in datas:
        direction, dist = data[0], int(data[1:])
        if direction == 'L':
            count += ((start-1) // 100) - ( (start - dist - 1) // 100)
            start = (start - dist)
        else:
            count += ( (start + dist) // 100) - (start // 100)
            start = (start + dist)
    return count

if __name__ == "__main__":
    if not os.path.isfile("inputs/day01.txt"):
        fetch(1)
    else:
        print("Input file already exists.")
    
    datas = read_input()
    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))