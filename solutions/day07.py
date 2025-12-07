import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def read_input():
    with open("inputs/day07.txt", "r") as f:
        lines = f.readlines()
    return [line.strip('\n') for line in lines]
    
def solve_part1(datas):
    pos = datas[0].find('S')
    ans = 0
    curr, lvl = [pos], 0

    while lvl + 1 < len(datas):
        next_curr = []
        for p in curr:
            if datas[lvl+1][p] == '.':
                if p not in next_curr:
                    next_curr.append(p)
            else:
                ans += 1
                if p-1 not in next_curr:
                    next_curr.append(p-1)
                if p+1 not in next_curr:
                    next_curr.append(p+1)
        curr = next_curr
        lvl += 1
        
    return ans

def solve_part2(datas):
    pos = datas[0].find('S')

    curr, lvl = [0 for i in range(len(datas[0]))], 0
    curr[pos] = 1

    while lvl < len(datas):
        next_curr = [0 for _ in range(len(datas[0]))]
        for p, val in enumerate(curr):
            if datas[lvl+1][p] == '.':
                next_curr[p] += val
            else:
                next_curr[p-1] += val
                next_curr[p+1] += val
        curr = next_curr
        lvl += 1
        
        if lvl + 1 == len(datas):
            break
        
    return sum(curr)

if __name__ == "__main__":
    if not os.path.isfile("inputs/day07.txt"):
        fetch(7)
    else:
        print("Input file already exists.")
    
    datas = read_input()
    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))