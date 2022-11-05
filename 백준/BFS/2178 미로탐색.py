# https://www.acmicpc.net/problem/2178
from collections import deque

import sys
input = sys.stdin.readline

# 이동해야할 위치. 시작은 1,1에서 출발
n, m = map(int, input().split())
map = [input().strip() for _ in range(n)]
# 더해나가며 계산 결과 chk[n][m]이 답이된다!
chk = [[0] * m for _ in range(n)]

# 오른, 아래, 왼, 위
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs(y, x):
    q = deque()
    q.append((0, 0))
    chk[0][0] = 1

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if map[ny][nx] == '1' and chk[ny][nx] == 0:
                    chk[ny][nx] = chk[ey][ex] + 1
                    q.append((ny,nx))
    
    return chk[y][x]

# 목표까지 BFS를 돌며 목표에 도착 시 카운트를 출력하고 종료
# 시작 인덱스는 0,0 이므로 각각 n과 m에 -1 해줌
print(bfs(n-1, m-1))

