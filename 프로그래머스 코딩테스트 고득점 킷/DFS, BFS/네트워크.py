def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            answer += 1
            dfs(computers, visited, i)

    return answer

def dfs(computers, visited, i):
    visited[i] = True
    for computer, conn_check in enumerate(computers[i]):
        if conn_check == 1 and not visited[computer]:
            dfs(computers, visited, computer)

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))