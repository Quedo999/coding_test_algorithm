#https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
cnt = 0

coins.reverse()

for i in coins:
    if i > k:
        continue
    cnt += k // i
    k %= i

print(cnt)