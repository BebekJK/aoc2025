import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def read_input():
    with open("inputs/day04.txt", "r") as f: 
        lines = f.readlines()
    return [line.strip('\n') for line in lines]
    
def solve_part1(datas):
    ans = 0
    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
    r, c = len(datas), len(datas[0])
    for i in range(r):
        for j in range(c):
            curr = datas[i][j]
            if curr != '@':
                continue

            count = 0
            for d in range(8):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < r and 0 <= nj < c:
                    if datas[ni][nj] == '@':
                        count += 1

            if count < 4:
                ans += 1

    return ans

def solve_part2(datas):
    ans = 0
    dx, dy = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]
    r, c = len(datas), len(datas[0])
    new_datas = []

    for i in range(r):
        new_row = []
        for j in range(c):
            curr = datas[i][j]
            if curr != '@':
                new_row.append(curr)
                continue

            count = 0
            for d in range(8):
                ni, nj = i + dx[d], j + dy[d]
                if 0 <= ni < r and 0 <= nj < c:
                    if datas[ni][nj] == '@':
                        count += 1

            if count < 4:
                ans += 1
                new_row.append('.')
            else:
                new_row.append(curr)
        new_datas.append(new_row)
    
    if ans == 0:
        return 0
    return ans + solve_part2([''.join(row) for row in new_datas])

if __name__ == "__main__":
    if not os.path.isfile("inputs/day04.txt"): 
        fetch(4)  
    else:
        print("Input file already exists.")
    
    datas = read_input()
    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))