# 동북서남, 이동 방향
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
move_type = ['R', 'U', 'L', 'D']

x, y = 1, 1

n = int(input())
move = input().split()

# 이동 계획 확인
for plan in move:
    # 이동 후 좌표
    for i in range(len(move_type)):
        if plan == move_type[i]:
            if x + dx[i] < 1 or y + dy[i] < 1 or x + dx[i] > n or y + dy[i] > n:
                continue
            else:
                x += dx[i]
                y += dy[i]

print(x, y)