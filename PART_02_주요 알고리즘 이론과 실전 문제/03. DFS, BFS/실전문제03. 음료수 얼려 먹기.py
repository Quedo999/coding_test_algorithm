from posixpath import split


n, m = map(int, input().split())
ice_map = [list(map(int, input())) for i in range(n)]
result = 0

# 연결 탐색을 위한 dfs 구현
def dfs(a, b):
    if a < 0 or b < 0 or a >= n or b >= m:
        return False
    if ice_map[a][b] == 0:
        ice_map[a][b] = 1
        dfs(a+1, b)
        dfs(a-1, b)
        dfs(a, b+1)
        dfs(a, b-1)
        return True
    return False

for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)