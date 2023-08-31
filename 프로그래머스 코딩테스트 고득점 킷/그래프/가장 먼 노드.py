from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    cnt_count = [0,0]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    q = deque()
    q.append([graph[1], 0])
    visited[1] = True

    while q:
        v, cnt = q.popleft()
        if cnt > cnt_count[0]:
            cnt_count[0] = cnt
            cnt_count[1] = 1
        elif cnt == cnt_count[0]:
            cnt_count[1] += 1

        for i in v:
            if not visited[i]:
                print(i, end=" ")
                visited[i] = True
                q.append([graph[i], cnt + 1])

    return cnt_count[1]

n, edge = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))