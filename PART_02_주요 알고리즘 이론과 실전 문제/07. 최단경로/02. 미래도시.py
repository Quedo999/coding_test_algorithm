# 259 page
# 회사의 갯수, 도로의 수

INF = int(1e9)
n, m = map(int, input().split())

# 플로이드 워셜을 위한 배열 선언
graph = [[INF] * (n + 1) for _ in range(n+1)]

# 자기자신으로 향하는 곳은 0으로 초기화!
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 회사간 도로를 이동하는 속도는 무조건 1! 양방향 이동이 가능하므로 이게 맞춰서 간선 설정을 함
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# x: 도달할 곳, k: 중간에 거쳐갈 곳
x, k = map(int, input().split())

# 플로이드 워셜 진행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 문제의 요구사항 1 -> k -> x로 이동하는 최소이동시간
# 이동 방법이 없다면 -1 출력
# g[1][k] + g[k][x]
if graph[1][k] == INF or graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])