# https://www.acmicpc.net/problem/1260


import sys
input = sys.stdin.readline
from collections import deque

n, m, start = list(map(int, input().split()))
maps = [list(map(int, input().split())) for _ in range(m)]
chk = [False] * n+1

print(chk)

#bfs
def bfs(start):
    q = deque()
    q.append(start)

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in maps:
            




# 출력
print(bfs(start))
print(dfs(start))