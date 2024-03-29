import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    clothes = {}

    n = int(input())

    for _ in range(n) :
        name, category = input().split()
        if category not in clothes :
            clothes[category] = set()
        clothes[category].add(name)

    count = 1
    for key in clothes.keys() :
        count *= len(clothes[key]) +1

    print(count-1)
