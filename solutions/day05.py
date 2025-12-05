import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def read_input():
    with open("inputs/day05.txt", "r") as f: 
        lines = f.readlines()
    datas = [line.strip('\n') for line in lines]
    line = datas.index('')
    part1 = datas[:line]
    part1 = [data.split('-') for data in part1]
    part1 = [(int(x), int(y)) for x, y in part1]

    part2 = datas[line+1:]
    part2 = [int(x) for x in part2]
    return part1, part2
    
def solve_part1(datas):
    data, query = datas[0], datas[1]
    ans = 0

    for q in query:
        for i in range(len(data)):
            x, y = data[i]
            if x <= q <= y:
                ans += 1
                break
    return ans

def solve_part2(datas):
    data, _ = datas
    data.sort()

    merged = []
    le, ri = data[0]
    for x, y in data[1:]:
        if x <= ri:
            ri = max(ri, y)
        else:
            merged.append((le, ri))
            le, ri = x, y
    merged.append((le, ri))

    ans = sum(y - x + 1 for x, y in merged)
    return ans

if __name__ == "__main__":
    if not os.path.isfile("inputs/day05.txt"): 
        fetch(5)  
    else:
        print("Input file already exists.")
    
    datas = read_input()

    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))