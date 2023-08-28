# 개수 리턴
def dfs(graph, v, visited: list):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

    return visited.count(True)
    

def solution(n, wires):
    result = []

    for i in range(len(wires)):
        graph = [[] for _ in range(n + 1)]
        visited = [False] * (n+1)
        wire = wires[:i] + wires[i+1:]

        for v1, v2 in wire:
            graph[v1].append(v2)
            graph[v2].append(v1)
        w1 = dfs(graph, wires[i][0], visited)
        w2 = abs(w1 - n)
        result.append(abs(w1 - w2))
    return min(result)


n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
print(solution(n, wires))