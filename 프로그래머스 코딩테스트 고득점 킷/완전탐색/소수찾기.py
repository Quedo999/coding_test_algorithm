from itertools import permutations
import math

def solution(numbers):
    answer = 0
    a = [int(i) for i in numbers]
    for i in range(1, len(numbers)):
        a += [int(''.join(i)) for i in list(permutations(numbers, i + 1))]
    a = set(a)
    
    for i in a:
        if i == 0 or i == 1:
            continue
        
        if prime(i):
            answer += 1

    return answer

def prime(num):
    for x in range(2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False
    return True

numbers = "17"

print(solution(numbers))