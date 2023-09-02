# https://www.acmicpc.net/problem/1654
from sys import stdin
input = stdin.readline

# k: 랜선 개수, n: 필요한 랜선 개수(n개 이상이어도 됨)
k, n = map(int, input().split())
lans = [int(input()) for _ in range(k)]

# 패러매트릭 서치를 위한 변수 초기화.
right = 2 ** 31 - 1
left = 1
result = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for l in lans:
        cnt += l // mid
    
    if cnt >= n:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)