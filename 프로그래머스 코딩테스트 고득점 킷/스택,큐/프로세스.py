"""
1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
"""

def solution(priorities, location):
    answer = 1
    p = [[i, e] for i, e in enumerate(priorities)]
    pCnt = []
    
    for i in priorities:
        priorities.count(i)
        pCnt.append((i, priorities.count(i)))
    
    pCnt = set(pCnt)
    pCnt = [list(i) for i in pCnt]
    pCnt = sorted(pCnt, key=lambda x: x[0], reverse=True)
    
    while True:
        i = p.pop(0)
        if i[1] == pCnt[0][0]:
            if i[0] == location:
                return answer
            else:
                answer += 1
            if pCnt[0][1] - 1 == 0:
                pCnt.pop(0)
            else:
                pCnt[0][1] = pCnt[0][1] - 1
        else:
            p.append(i)


priorities = [2,1,3,2]
location = 2

print(solution(priorities, location))