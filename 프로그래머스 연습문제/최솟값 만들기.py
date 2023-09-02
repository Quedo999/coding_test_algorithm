from collections import deque

def solution(A,B):
    answer = 0
    q_A = deque(sorted(A))
    q_B = deque(sorted(B))
    
    while q_A:
        a = q_A.popleft()
        b = q_B.pop()
        answer += a * b
    return answer

A, B = [1, 4, 2], [5, 4, 4]
print(solution(A,B))