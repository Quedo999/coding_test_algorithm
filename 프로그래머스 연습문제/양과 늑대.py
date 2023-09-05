def solution(info, edges):
    answer = 1
    n = len(info)
    # 비트마스킹을 위한 visited 생성.
    visited = [0] * (1 << 17)

    l_node = [-1] * n
    r_node = [-1] * n
    for a, b in edges:
        if l_node[a] == -1:
            l_node[a] = b
        else:
            r_node[a] = b

    def dfs(state):
        if visited[state]:
            return None
        visited[state] = 1
        wolf = 0
        node_cnt = 0

        for i in range(n):
            # 현재 state에 i번노드의 원소가 포함됬는지 확인
            if state & (1 << i):
                wolf += info[i]
                node_cnt += 1
        # 늑대의 수가 현재 노드의 절반을 넘어가면 방문할 수 없으니 종료
        if 2*wolf >= node_cnt:
            return None
        # 현재 양의 수를 많은 것으로 answer 갱신
        nonlocal answer
        answer = max(answer, node_cnt - wolf)

        # 계속해서 탐색
        for i in range(n):
            if not state & (1 << i):
                continue
            # 왼쪽 노드가 있다면. 왼쪽노드로 상태이동 후 진행
            if l_node[i] != -1:
                # l_node에 저장된 왼쪽 노드만큼 state 집합으로 추가
                dfs(state | (1<<l_node[i]))
            # 오른쪽 노드가 있다면. 오른쪽 노드로 상태이동 후 진행
            if r_node[i] != -1:
                # r_node에 저장된 오른쪽 노드만큼 state 집합으로 추가
                dfs(state | (1<<r_node[i]))
    
    dfs(1)
    return answer

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
print(solution(info, edges))