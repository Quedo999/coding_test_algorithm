# https://school.programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append([0,0])

    while q:
        idx, num = q.popleft()
        if idx < len(numbers):
            q.append([idx+1, num+numbers[idx]])
            q.append([idx+1, num-numbers[idx]])

        if idx == len(numbers):
            if num == target:
                answer += 1

    return answer


numbers = [[1,1,1,1,1], [4,1,2,1]]
target = [3, 4]
re = [5, 2]

print(solution(numbers[0], target[0]))