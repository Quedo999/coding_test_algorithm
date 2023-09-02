def solution(arr):
    answer = 1
    for i in arr:
        answer = LCM(answer, i)

    return answer

def GCD(a, b):
    while b:
        a, b = b, a % b
    return a

def LCM(a, b):
    return a * b // GCD(a, b)

arr = [2, 6, 8, 14]
print(solution(ConnectionAbortedError))