#https://www.acmicpc.net/problem/2231
n = input()
start = max(1, int(n) - (len(n) * 9))

def fun(start, n):
    for i in range(start, n+1):
        if sum([int(num) for num in str(i)]) + i == n:
            return i
    return 0

print(fun(start, int(n)))