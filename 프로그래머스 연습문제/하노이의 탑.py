def solution(n):
    answer = []
    answer = hanoi(n, answer, 1, 2, 3)
    return answer

def hanoi(n, answer, first, second, third):
    if n == 1:
        answer.append([first, third])
        return answer
    
    hanoi(n - 1, answer, first, third, second)
    answer.append([first, third])
    hanoi(n - 1, answer, second, first, third)
    return answer


n = 3
print(solution(n))