# https://www.acmicpc.net/problem/2606

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
net = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(net):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
q = deque()
q.append(1)
visited[1] = True
cnt = 0

while q:
    v = q.popleft()
    for g in graph[v]:
        if not visited[g]:
            visited[g] = True
            cnt += 1
            q.append(g)

print(cnt)