import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def read_input():
    with open("inputs/day06.txt", "r") as f:
        lines = f.readlines()
    return [line.strip('\n') for line in lines]
    
def solve_part1(datas):
    operators, values = datas[-1], datas[:-1]
    operators = [op for op in operators.split(' ') if op]
    values = [[v for v in val.split(' ') if v] for val in values] 

    ans = 0
    for i in range(len(operators)):
        if operators[i] == '+':
            tmp = 0
            tmp = sum(int(v[i]) for v in values)
        else:
            tmp = 1
            for val in values:
                tmp *= int(val[i])
        ans += tmp
    return ans

def solve_part2(datas):
    operators, values = datas[-1], datas[:-1]
    operators = [op for op in operators.split(' ') if op]

    sep = []
    for i in range(len(values[0])):
        if all(val[i] == ' ' for val in values) == True:
            sep.append(i)
    sep.append(len(values[0]))

    ans = 0
    prev = -1
    for i in range(len(sep)):
        op = operators[i]
        nums = ['' for _ in range(sep[i] - prev - 1)]
        for j in range(prev + 1, sep[i]):
            for val in values:
                nums[j - prev - 1] += val[j]
        
        nums = [int(num) for num in nums]
        if op == '+':
            ans += sum(nums)
        else:
            tmp = 1
            for num in nums:
                tmp *= num
            ans += tmp
        prev = sep[i]
    return ans

if __name__ == "__main__":
    if not os.path.isfile("inputs/day06.txt"):
        fetch(6)
    else:
        print("Input file already exists.")
    
    datas = read_input()
    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))