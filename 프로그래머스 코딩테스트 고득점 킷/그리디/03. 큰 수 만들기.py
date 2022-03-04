# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3

# 풀이
from itertools import permutations, combinations
def solution(number, k): # 문자열 형식의 수 number, 제거할 숫자 개수 k, combinations 이용
    numbers = list(combinations(map(str, number), len(number) - k))
    numbers = ["".join(i) for i in numbers]
    return max(numbers)

print(solution("1924", 2))