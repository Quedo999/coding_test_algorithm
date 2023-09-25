# https://www.acmicpc.net/problem/28472
from collections import defaultdict
from sys import stdin
input = stdin.readline

n, r = map(int, input().split())

graph = defaultdict(list)
for _ in range(n-1):
    u, v = sorted(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

node_value = [-1 for _ in range(n+1)]
for _ in range(int(input())):
    k, t = map(int, input().split())
    node_value[k] = t

q = []
for _ in range(int(input())):
    q.append(int(input()))

def minimax(pre, node, dept):
    if node_value[node] != -1:
        return node_value[node]
    tmp = []
    for g in graph[node]:
        if g == pre:
            continue
        tmp.append(minimax(node, g, dept+1))
    if dept % 2 == 0 :
        node_value[node] = max(tmp)
    else:
        node_value[node] = min(tmp)
    return node_value[node]

minimax(r, r, 0)

for i in q:
    print(node_value[i])