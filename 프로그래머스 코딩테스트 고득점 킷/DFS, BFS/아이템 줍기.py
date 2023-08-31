from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    rec_map = [[0 for _ in range(102)] for _ in range(102)]
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    for x_y in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, x_y)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    rec_map[i][j] = -1
                elif rec_map[i][j] != -1:
                    rec_map[i][j] = 1

    # bfs
    q = deque([[characterX, characterY, 0]])
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        x, y, cnt = q.popleft()
        if [x, y] == [itemX, itemY]:
            answer = cnt // 2
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if rec_map[nx][ny] == 1:
                q.append([nx, ny, cnt + 1])
        rec_map[x][y] = -1

    return answer


rectangle = [[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]]
characterX, characterY, itemX, itemY = 9,7,6,1
print(solution(rectangle, characterX, characterY, itemX, itemY))