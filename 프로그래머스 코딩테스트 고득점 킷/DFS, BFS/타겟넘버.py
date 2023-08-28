# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# DFS 풀이
# def dfs(sum_number, numbers, target):
#     if len(numbers) == 0:
#         if sum_number == target:
#             global answer
#             answer += 1
#     else:
#         dfs(sum_number + numbers[0],numbers[1:], target)
#         dfs(sum_number - numbers[0],numbers[1:], target)

# def solution(numbers, target):
#     global answer
#     answer = 0
#     dfs(0, numbers, target)

#     return answer


# BFS 풀이
from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque([[0,0]])
    len_numbers = len(numbers)

    while q:
        number, idx = q.popleft()
        if idx == len_numbers:
            if number == target:
                answer += 1
            continue
        else:
            q.append([number + numbers[idx], idx + 1])
            q.append([number - numbers[idx], idx + 1])

    return answer 


numbers = [[1,1,1,1,1], [4,1,2,1]]
target = [3, 4]
re = [5, 2]

print(solution(numbers[1], target[1]))