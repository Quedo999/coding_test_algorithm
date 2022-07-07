# 이동 경로
dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

point_data = input()

cnt = 0

x = int(point_data[1])
y = int(ord(point_data[0])) - 96

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue

    cnt += 1

print(cnt)