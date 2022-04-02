n, m, v = map(int, input().split())

nodes = [[]]

for _ in range(m):
    nodes.append(list(map(int, input().split())))

print(nodes)

# dfs
def dfs(nodes, visited, start):
    visited[start] = True
    print(start, end=' ')
    for i in nodes[start]:
        if not visited[i]:
            dfs(nodes, visited, i)

# 정점 개수 + 1개
visited = [False] * 1001

dfs(nodes, visited, v)