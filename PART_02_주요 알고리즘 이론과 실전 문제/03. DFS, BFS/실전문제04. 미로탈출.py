from collections import deque

# 입력
n, m = map(int, input().split())
d_map = [list(map(int, input())) for i in range(n)]

# 이동하는 것 이므로 이동방향 지정
# 동북서남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 최단경로이므로 bfs 이용
def bfs(x, y):
    # bfs를 위한 queue 생성
    q = deque()
    q.append((x, y))
    # queue가 빌때까지 계속해서 반복
    while q:
        x, y = q.popleft()
        # 현 위치에서 갈 수 있는 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로를 벗어나는 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 괴물이 있는경우 무시
            if d_map[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우 방문처리함
            if d_map[nx][ny] == 1:
                d_map[nx][ny] = d_map[x][y] + 1
                q.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단거리 반환
    return d_map[n-1][m-1]

print(bfs(0, 0))