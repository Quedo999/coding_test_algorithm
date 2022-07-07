# 4
n = 5 # 노드 개수
edges = [[0,1],[0,2],[1,3],[1,4]] # 간선 정보

from collections import deque

def solution(n, edges):
    answer = 0

    # dfs 돌리기 원활하도록 그래프 생성
    graph = [[] for _ in range(n)]
    for i in edges:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    def dfs(graph, start):
        dist = [-1] * n
        dist[start] = 0
        q = deque([start])
        while q:
            now = q.popleft()
            for n_node in graph[now]:
                if dist[n_node] == -1:
                    dist[n_node] = dist[now] + 1
                    q.append(n_node)
        return dist

    for i in range(n):
        d_list = dfs(graph, i)
        for j in d_list:
            if j >= 2:
                answer += 1
                
    return answer

print(solution(n, edges))