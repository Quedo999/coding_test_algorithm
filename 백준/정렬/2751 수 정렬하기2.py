from sys import stdin
input = stdin.readline

n = int(input())
ls = sorted([int(input()) for _ in range(n)])

for i in ls:
    print(i)