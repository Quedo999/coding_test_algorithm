def solution(tickets):
    answer = ["ICN"]
    visited = [False for _ in range(len(tickets))]
    tickets = sorted(tickets, key=lambda x:x[1])

    for idx, ticket in enumerate(tickets):
        if ticket[0] == "ICN":
            answer.append(ticket[1])
            dfs(ticket[1], tickets, idx, visited, answer)
            if set(visited) == {True}:
                break
            else:
                answer = ["ICN"]
                visited = [False for _ in range(len(tickets))]

    return answer

def dfs(airplan_point, tickets, idx, visited, answer):
    if visited[idx] == False:
        visited[idx] = True
    for idx, ticket in enumerate(tickets):
        if ticket[0] == airplan_point and not visited[idx]:
            answer.append(ticket[1])
            dfs(ticket[1], tickets, idx, visited, answer)
            if set(visited) == {True}:
                return 0
            else:
                visited[idx] = False
                answer.pop()

tickets = [["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"], ["BOO", "DOO"]]
print(solution(tickets))

