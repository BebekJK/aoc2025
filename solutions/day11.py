import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def read_input():
    with open("inputs/day11.txt", "r") as f: # CHANGE HERE <--
        lines = f.readlines()
    return [line.strip('\n') for line in lines]
    
def solve_part1(datas):
    adj = {}
    for data in datas:
        data = data.split()
        src, dest = data[0][:-1], data[1:]
        if src not in adj:
            adj[src] = []
        for d in dest:
            adj[src].append(d)
    
    q = ['you']
    ans = 0
    while q:
        curr = q.pop()
        for neighbor in adj[curr]:
            if neighbor == 'out':
                ans += 1
                continue
            q.append(neighbor)

    return ans

def solve_part2(datas):
    adj = {}
    for data in datas:
        data = data.split()
        src, dest = data[0][:-1], data[1:]
        if src not in adj:
            adj[src] = []
        for d in dest:
            adj[src].append(d)

    memo = {}

    def dfs(curr, mask):
        if curr == 'out':
            return 1 if mask == 3 else 0
        
        state = (curr, mask)
        if state in memo:
            return memo[state]
        
        count = 0
        if curr in adj:
            for neighbor in adj[curr]:
                new_mask = mask
                if neighbor == 'fft':
                    new_mask |= 1
                elif neighbor == 'dac':
                    new_mask |= 2
                count += dfs(neighbor, new_mask)
        
        memo[state] = count
        return count

    return dfs('svr', 0)

if __name__ == "__main__":
    if not os.path.isfile("inputs/day11.txt"): # CHANGE HERE <--
        fetch(11)  # CHANGE HERE <--
    else:
        print("Input file already exists.")
    
    datas = read_input()
    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))