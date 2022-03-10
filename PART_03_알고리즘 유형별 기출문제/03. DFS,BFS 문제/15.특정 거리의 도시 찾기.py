# 최단거리 이므로 bfs 이용
from collections import deque

# 도시개수 n, 도로 개수 m, 거리 정보 k, 출발 도시 x
n, m, k, x = map(int, input().split())

# 도시 개수만큼 리스트 생성
city_map = [[] for _ in range(n+1)]

# 도로정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    city_map[a].append(b)

# 도시 사이의 최단거리 초기화
distance = [-1] * (n+1)
# 시작지점 x 는 0으로 초기화
distance[x] = 0

# bfs 수행
q = deque([x])
while q:
    # 현재 도시 설정
    city = q.popleft()
    # 현 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in city_map[city]:
        # 방문하지 않은 도시라면
        if distance[next_node] == -1:
            distance[next_node] = distance[city] + 1
            q.append(next_node)

# 최단거리가 없을 경우 체크
chk = False

for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        chk = True

if chk == False:
    print(-1)
