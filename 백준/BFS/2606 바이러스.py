# https://www.acmicpc.net/problem/2606

from collections import deque

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

map = [list(map(int, input().split())) for _ in range(m)]
chk = [False for _ in range(n + 1)]

# bfs를 통해 1번에 연결된 컴퓨터 수만 구하면 됨
def bfs():
    q = deque()
    q.append(1)
    cnt = 0
    while q:
        v = q.popleft()
        for i in map:
            if i[0] == v and chk[i[1]] == False:
                q.append(i[1])
                chk[i[1]] = True
            elif i[1] == v and chk[i[0]] == False:
                q.append(i[0])
                chk[i[0]] = True
    return chk.count(True) - 1

print(bfs())