import os
import sys
sys.setrecursionlimit(200000)
project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def read_input():
    with open("inputs/day09.txt", "r") as f: # CHANGE HERE <--
        lines = f.readlines()
    return [line.strip('\n') for line in lines]
    
def solve_part1(datas):
    datas = [data.split(',') for data in datas]
    ans = 0
    n = len(datas)
    
    for i in range(n):
        for j in range(i+1, n):
            ans = max(ans, (abs(int(datas[i][0]) - int(datas[j][0])) + 1) * (abs(int(datas[i][1]) - int(datas[j][1])) + 1))
    return ans

def solve_part2(datas):
    datas = [data.split(',') for data in datas]
    ans = 0
    n = len(datas)

    def compress(arr):
        vals = sorted(set(arr))
        mapping = {v: i for i, v in enumerate(vals)}
        return [2*mapping[v] for v in arr]
    
    datas_x = [int(data[0]) for data in datas]
    datas_y = [int(data[1]) for data in datas]
    comp_x = compress(datas_x)
    comp_y = compress(datas_y)

    grid = [['.'] * (max(comp_y) + 1) for _ in range(max(comp_x) + 1)]
    for i in range(1, n):
        if comp_x[i] == comp_x[i-1]:
            for j in range(min(comp_y[i], comp_y[i-1]), max(comp_y[i], comp_y[i-1]) + 1):
                grid[comp_x[i]][j] = '#'
        elif comp_y[i] == comp_y[i-1]:
            for j in range(min(comp_x[i], comp_x[i-1]), max(comp_x[i], comp_x[i-1]) + 1):
                grid[j][comp_y[i]] = '#'
    
    if comp_x[-1] == comp_x[0]:
        for j in range(min(comp_y[-1], comp_y[0]), max(comp_y[-1], comp_y[0]) + 1):
            grid[comp_x[-1]][j] = '#'
    elif comp_y[-1] == comp_y[0]:
        for j in range(min(comp_x[-1], comp_x[0]), max(comp_x[-1], comp_x[0]) + 1):
            grid[j][comp_y[-1]] = '#'

    def fill(x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != '.':
            return
        grid[x][y] = '#'
        fill(x+1, y)
        fill(x-1, y)
        fill(x, y+1)
        fill(x, y-1)
    fill(245, 1)

    def query(x1, y1, x2, y2):
        res = pref[x2][y2]
        if x1 > 0:
            res -= pref[x1-1][y2]
        if y1 > 0:
            res -= pref[x2][y1-1]
        if x1 > 0 and y1 > 0:
            res += pref[x1-1][y1-1]
        return res
    
    pref = [[0] * (len(grid[0])) for _ in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            pref[i][j] = (1 if grid[i][j] == '#' else 0)
            if i > 0:
                pref[i][j] += pref[i-1][j]
            if j > 0:
                pref[i][j] += pref[i][j-1]
            if i > 0 and j > 0:
                pref[i][j] -= pref[i-1][j-1]
    
    for i in range(n):
        for j in range(i+1, n):
            x1, y1 = comp_x[i], comp_y[i]
            x2, y2 = comp_x[j], comp_y[j]
            min_x, min_y = min(x1, x2), min(y1, y2)
            max_x, max_y = max(x1, x2), max(y1, y2)
            if query(min_x, min_y, max_x, max_y) == (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1):
                ans = max(ans, (abs(datas_x[i] - datas_x[j]) + 1) * (abs(datas_y[i] - datas_y[j]) + 1))
    grid = '\n'.join([''.join(row) for row in grid])
    with open('day09_grid.txt', 'w') as f:
        f.write(grid)
    return ans

if __name__ == "__main__":
    if not os.path.isfile("inputs/day09.txt"): # CHANGE HERE <--
        fetch(9)  # CHANGE HERE <--
    else:
        print("Input file already exists.")
    
    datas = read_input()
    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))