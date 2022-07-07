#https://www.acmicpc.net/problem/2750

n = int(input())
ls = [int(input()) for _ in range(n)]
ls.sort()

for i in ls:
    print(i)