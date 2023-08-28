from collections import deque

def solution(people, limit):
    answer = 0
    pDeque = deque(sorted(people))
    
    # answer 계산
    while pDeque:
        if len(pDeque) == 1:
            answer += 1
            break

        # 최소값 + 최대값 <= limit 면 두개 다 pop, answer + 1
        # 아니라면 최소값에서 더해져서 비교된 것이기 때문에 최대값만 pop 동시에 answer + 1
        if pDeque[0] + pDeque[-1] <= limit:
            pDeque.popleft()
            pDeque.pop()
            answer += 1
            continue

        pDeque.pop()
        answer += 1

    return answer

people, limit = [70,80,50], 100

print(solution(people, limit))