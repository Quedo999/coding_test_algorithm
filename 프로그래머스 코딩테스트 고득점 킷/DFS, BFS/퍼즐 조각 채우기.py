from collections import deque
import copy

def solution(game_board, table):
    answer = 0
    g_visited = [[False] * len(table) for _ in range(len(table))]
    t_visited = copy.deepcopy(g_visited)
    x_len = len(table)
    y_len = len(table[0])

    # 게임보드와 테이블에 있는 블록 빼기. 
    board_blocks = bfs(g_visited, game_board, x_len, y_len, 1)
    table_blocks = bfs(t_visited, table, x_len, y_len, 0)

    board_blocks = [block_align(block) for block in board_blocks]
    table_blocks = [block_align(block) for block in table_blocks]

    for block in table_blocks:
        if block in board_blocks:
            board_blocks.remove(block)
            answer += len(block)
            continue
        for _ in range(3):
            block = block_rotate(block)
            if block in board_blocks:
                board_blocks.remove(block)
                answer += len(block)
                break

    return answer

def bfs(visited, board, x_len, y_len, ex_tile):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0 ,0]
    blocks = []
    q = deque()

    for i in range(x_len):
        for j in range(y_len):
            if visited[i][j] or board[i][j] == ex_tile:
                if not visited[i][j]:
                    visited[i][j] = True
                continue
            
            q.append([i, j])
            block = []
            # bfs
            while q:
                x, y = q.popleft()
                visited[x][y] = True
                block.append([x,y])
                for next in range(4):
                    nx = x+dx[next]
                    ny = y+dy[next]
                    if nx < 0 or ny < 0 or nx >= x_len or ny >= y_len:
                        continue
                    if not visited[nx][ny]:
                        visited[nx][ny] = True
                        if board[nx][ny] == ex_tile:
                            continue
                        else:
                            q.append([nx, ny])
            blocks.append(block)
    return blocks

# 블록 좌표 정렬시키기:
def block_align(block):
    min_x, min_y = [min(i) for i in zip(*block)]
    return sorted([[a-min_x, b-min_y] for a, b in block])

# 블록을 시계방향으로 90도 회전
def block_rotate(block):
    n = max(block, key=lambda x:x[0])[0]
    return block_align([[b, n - a] for a, b in block])


game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]
table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
print(solution(game_board, table))
print(solution([[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]]))