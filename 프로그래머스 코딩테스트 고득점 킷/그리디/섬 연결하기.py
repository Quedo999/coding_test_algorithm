"""
크루스칼 알고리즘 사용
최소 신장트리를 찾는 알고리즘이며 그래프의 간선을 하나 씩 늘리며 가중치가 최소인 간선부터 추가하는 그리디 방식
간선을 추가하는 각 단계에서 사이클을 이루지 않는 최소 비용 간선을 선택해 MST(최소 신장 트리)를 만들어냄

1. 그래프 간선들의 가중치의 오름차순으로 정렬
2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선 선택
    - 가장 낮은 가중치를 먼저 선택
    - 사이클을 형성하는 간선을 제외
    - 사이클을 판단할 때는 보통 union - find 를 활용
3. 해당 간선을 현재 MST의 집합에 추가

"""

def solution(n, costs):
    answer = 0

    p = [i for i in range(n)]
    costs = sorted(costs, key=lambda x:x[2])
    rootNode = costs[0][0]

    for a, b, cost in costs:
        if set(p) == {rootNode}:
            break
        if find(p, a) != find(p, b):
            union(p, a, b)
            answer += cost

    return answer
        
def find(p, v):
    if p[v] == v:
        return v
    p[v] = find(p, p[v])
    return p[v]

def union(p, a, b):
    a = find(p, a)
    b = find(p, b)

    if a < b:
        p[b] = a
    else:
        p[a] = b

n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n, costs))