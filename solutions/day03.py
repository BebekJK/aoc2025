import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def read_input():
    with open("inputs/day03.txt", "r") as f:
        lines = f.readlines()
    return [line.strip('\n') for line in lines]

def dp(data, k):
    n = len(data)
    if k > n:
        return 0
    res = ''
    start = 0
    for t in range(k):
        end = n - (k - t)
        max_d = '0'
        max_i = start
        for i in range(start, end + 1):
            ch = data[i]
            if ch > max_d:
                max_d = ch
                max_i = i
                if max_d == '9':
                    break
        res = res + max_d
        start = max_i + 1
    return int(res)

def solve_part1(datas):
    ans = 0
    for data in datas:
        ans += dp(data, 2)
    return ans

def solve_part2(datas):
    ans = 0
    for data in datas:
        ans += dp(data, 12)
    return ans

if __name__ == "__main__":
    if not os.path.isfile("inputs/day03.txt"):
        fetch(3)
    else:
        print("Input file already exists.")
    
    datas = read_input()
    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))