import os
import sys
sys.setrecursionlimit(200000)
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def read_input():
    with open("inputs/day10.txt", "r") as f: # CHANGE HERE <--
        lines = f.readlines()
    return [line.strip('\n') for line in lines]
    
def solve_part1(datas):
    ans = 0
    for data in datas:
        data = data.split(' ')[:-1]
        target = data[0][1:-1]
        target = sum([2**i for i in range(len(target)) if target[i] == '#'])

        operands = [sum([2**int(num) for num in od[1:-1].split(',')]) for od in data[1:]]
        
        vis = [False] * (2**10)
        q = [0]
        vis[0] = True
        curr = 0
        while len(q) > 0:
            n = len(q)
            for _ in range(n):
                u = q.pop(0)
                if u == target:
                    ans += curr
                    break
                else:
                    for op in operands:
                        if not vis[op ^ u]:
                            vis[op ^ u] = True
                            q.append(op ^ u)
            curr += 1
        
    return ans


def solve_part2(datas):
    pass

if __name__ == "__main__":
    if not os.path.isfile("inputs/day10.txt"): # CHANGE HERE <--
        fetch(10)  # CHANGE HERE <--
    else:
        print("Input file already exists.")
    
    datas = read_input()
    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))