#https://www.acmicpc.net/problem/2231


n = input()
l_n = len(n) * 9
result = 0

for i in range(int(n) - l_n, int(n) + 1):
    result += i
    for j in str(i):
        result += int(j)
    if result == int(n):
        print(i)
        break
    else:
        result = 0