def solution(n, s):
    if n > s:
        return [-1]
    num = s // n
    plus = s % n
    answer = [num for _ in range(n)]
    for i in range(1, plus+1):
        answer[-i] += 1
    return answer

n, s = 2, 9
print(solution(n ,s))