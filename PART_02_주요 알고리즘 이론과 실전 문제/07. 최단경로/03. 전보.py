# 262 page
# 데이터의 갯수가 많으므로 플로이드 워셜은 불가능
# 다익스트라로 구현

import sys
import heapq

# 데이터 양이 많으니 속도 개선을 위해 input을 sys.stdin.readline으로
input = sys.stdin.readline

# 다익스트라 알고리즘에서 사용할 우선순위큐 리스트 선언
q = []
# 무한값 설정
INF = int(1e9)

n, m, c = map(int,input().split())

# 각 도시간 통로의 연결 정보를 담을 리스트 생성
graph = [[] for _ in range(n + 1)]

# 최단거리 테이블을 도시의 개수만큼 무한으로 초기화
d = [INF] * (n + 1)

# 최단거리 테이블에서 시작 지점을 0으로 초기화 시켜줌
d[c] = 0

for _ in range(m):
    x, y, z = map(int, input().split())
    # 도시에 연결된 통로 정보를 입력받는다.
    graph[x].append((y, z))

# 다익스트라 함수 선언
def dijkstra(start):
    # 우선순위 큐(heap으로 구현)에 0, 시작점을 넣어줌. 시작점이므로 0으로 시작
    heapq.heappush(q, (0, start))

    # 우선순위 큐가 빌 때까지 돌림
    while q:
        # 가장 최단거리(시간)이 걸리는 노드를 우선순위 큐에서 꺼냄
        dist, now = heapq.heappop(q)
        # 현재의 노드가 이미 처리됐다면 무시한다
        if d[now] < dist:
            continue
        # 현재 노드와 인접한 노드들을 확인
        for city, line in graph[now]:
            cost = dist + line
            if cost < d[city]:
                d[city] = cost
                heapq.heappush(q, (cost, city))

dijkstra(c)

cnt = 0
result = []
for i in range(n + 1):
    if d[i] == INF or d[i] == 0:
        continue
    else:
        cnt += 1
        result.append(d[i])

print(cnt, max(result))