# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    chk = [[1]*m for _ in range(n)]
    dy = [0, 1, 0, -1]
    dx = [1, 0 , -1 ,0]

    q = deque()
    q.append([0, 0])
    
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if maps[ny][nx] == 1 and chk[ny][nx] == 1:
                    chk[ny][nx] += chk[y][x]
                    q.append([ny,nx])

    if chk[n-1][m-1] == 1:
        return -1

    return chk[n-1][m-1]



maps = [[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]],
        [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]]
ans = [11, -1]

for i in range(len(ans)):
    if solution(maps[i]) == ans[i]:
        print(solution(maps[i]), ans[i], '정답입니다.')