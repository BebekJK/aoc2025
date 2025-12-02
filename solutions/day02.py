import os
import sys

project_root = os.path.dirname(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils import fetch

def is_invalid(s):
    for i in range(1, len(s)//2 + 1):
        if len(s) % i == 0:
            pref = s[:i]
            curr = pref * (len(s) // i)
            if curr == s:
                return True
    return False

def count_invalid(a, b, max_multiple=2):
    first_invalid, last_invalid = 0, 0
    len_a, len_b = len(a), len(b)
    ans = 0
    
    for multiple in range(max_multiple, 1, -1):
        if len_a % multiple != 0:
            first_invalid = 10 ** (len_a // multiple)
        else:
            pref = a[:len_a // multiple]
            curr = pref * multiple
            if int(curr) < int(a):
                first_invalid = int(pref) + 1
            else:
                first_invalid = int(pref)
        
        if len_b % multiple != 0:
            last_invalid = 10 ** (len_b // multiple) - 1
        else:
            pref = b[:len_b // multiple]
            curr = pref * multiple
            if int(curr) > int(b):
                last_invalid = int(pref) - 1
            else:
                last_invalid = int(pref)
        
        if last_invalid < first_invalid:
            continue
        print(f"multiple: {multiple}, first_invalid: {first_invalid}, last_invalid: {last_invalid}")
        ans += sum([int(str(i) * multiple) if (len(str(i)) == 1 or (is_invalid(str(i)) == False)) else 0 for i in range(first_invalid, last_invalid + 1)])
    return ans

def read_input():
    with open("inputs/day02.txt", "r") as f:
        lines = f.readlines()
    lines = [line.strip('\n') for line in lines][0]
    lines = [line.split('-') for line in lines.split(",")]
    return [[(line[0]), (line[1])] for line in lines]

def solve_part1(datas):
    return sum([count_invalid(data[0], data[1]) for data in datas])

def solve_part2(datas):
    return sum([count_invalid(data[0], data[1], max_multiple=100) for data in datas])

if __name__ == "__main__":
    if not os.path.isfile("inputs/day02.txt"):
        fetch(2)
    else:
        print("Input file already exists.")
    
    datas = read_input()
    print("Part 1 solution:", solve_part1(datas))
    print("Part 2 solution:", solve_part2(datas))