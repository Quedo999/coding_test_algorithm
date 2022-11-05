# https://www.acmicpc.net/problem/1012

import sys
input = sys.stdin.readline

T = int(input())

dy = [0,1,0,-1]
dx = [1,0,-1,0]

def dfs(y,x):
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<=ny<N and 0<=nx<M and maps[ny][nx] == 1:
            maps[ny][nx] = 0
            dfs(ny,nx)

for _ in range(T):
    M, N, K = map(int, input().split())
    maps = [[0]*M for _ in range(N)]

    for i in range(K):
        y, x = map(int, input().split())
        maps[x][y] = 1

    cnt = 0

    for j in range(M):
        for i in range(N):
            if maps[i][j] == 1:
                cnt += 1
                maps[i][j] = 0
                dfs(i,j)
    print(cnt)