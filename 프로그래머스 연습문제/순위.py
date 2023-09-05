# 그래프 탐색을 통해 부모노드 + 자식노드 == n - 1 이면 해당 노드는 순위가 결정됐다고 볼 수 있음
# 자신을 제외한 모든 노드를 찾을 수 있기 때문

from collections import deque

def solution(n, results):
    answer = 0
    c_graph = [[] for _ in range(n+1)]
    p_graph = [[] for _ in range(n+1)]
    for p, c in results:
        c_graph[p].append(c)
        p_graph[c].append(p)

    q = deque()
    for i in range(1, n+1):
        visited = [False]*(n+1)
        c_cnt = 0
        p_cnt = 0

        # 자식노드들 찾기
        q.append(i)
        while q:
            v = q.popleft()
            if not visited[v]:
                visited[v] = True
                if i != v:
                    c_cnt += 1
                for j in c_graph[v]:
                    q.append(j)

        visited = [False]*(n+1)
        # 부모노드들 찾기
        q.append(i)
        while q:
            v = q.popleft()
            if not visited[v]:
                visited[v] = True
                if i != v:
                    p_cnt += 1
                for j in p_graph[v]:
                    q.append(j)

        if p_cnt + c_cnt == n - 1:
            answer += 1

    return answer


n, results = 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))