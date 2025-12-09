import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def read_input():
    with open("inputs/day08.txt", "r") as f:
        lines = f.readlines()
    return [line.strip('\n') for line in lines]
    
def solve_part1(datas):
    datas = [line.split(',') for line in datas]
    datas = [[int(num) for num in line] for line in datas]

    

    parent = [i for i in range(len(datas))]
    def find(p):
        if parent[p] != p:
            parent[p] = find(parent[p])
        return parent[p]
    
    connections = []
    for i in range(len(datas)):
        for j in range(len(datas)):
            if i >= j:
                continue
            diff = (datas[i][0] - datas[j][0])**2 + (datas[i][1] - datas[j][1])**2 + (datas[i][2] - datas[j][2])**2
            connections.append((diff, i, j))

    connections.sort()
    connections = connections[:(len(datas))]
    for _, i, j in connections:
        pi = find(i)
        pj = find(j)
        if pi != pj:
            pi, pj = min(pi, pj), max(pi, pj)
            parent[pi] = pj
    count = [0 for _ in range(len(datas))]
    for i in range(len(datas)):
        count[find(i)] += 1
    
    count.sort()
    return count[-1] * count[-2] * count[-3]

def solve_part2(datas):
    datas = [line.split(',') for line in datas]
    datas = [[int(num) for num in line] for line in datas]

    

    parent = [i for i in range(len(datas))]
    def find(p):
        if parent[p] != p:
            parent[p] = find(parent[p])
        return parent[p]
    
    connections = []
    for i in range(len(datas)):
        for j in range(len(datas)):
            if i >= j:
                continue
            diff = (datas[i][0] - datas[j][0])**2 + (datas[i][1] - datas[j][1])**2 + (datas[i][2] - datas[j][2])**2
            connections.append((diff, i, j))

    connections.sort()
    count = [1 for _ in range(len(datas))]
    for _, i, j in connections:
        pi = find(i)
        pj = find(j)
        if pi != pj:
            pi, pj = min(pi, pj), max(pi, pj)
            parent[pi] = pj
            count[pj] += count[pi]
            count[pi] = 0

            if count[pj] == len(datas):
                return datas[i][0] * datas[j][0]

if __name__ == "__main__":
    if not os.path.isfile("inputs/day08.txt"):
        fetch(8)
    else:
        print("Input file already exists.")
    
    datas = read_input()
    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))