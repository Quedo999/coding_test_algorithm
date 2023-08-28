# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

# 풀이
from collections import deque

def solution(number, k):
    numbers = deque(number)
    finalnum = deque([])
    
    while True:
        finalnum.append(numbers.popleft())
        if not numbers:
            break
        if finalnum[-1] < numbers[0]:
            for i in range(len(finalnum)-1, -1, -1):
                if k == 0:
                    return "".join(finalnum + numbers)
                if finalnum[i] < numbers[0]:
                    finalnum.pop()
                    k -= 1
                else:
                    break
    
    if k > 0:
        for _ in range(k):
            finalnum.pop()
    return "".join(finalnum)

print(solution("1924", 2))