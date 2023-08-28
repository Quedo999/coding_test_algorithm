"""
progresses : 현재 작업된 작업량
speeds : 작업속도
index : 작업 번호
"""

def solution(progresses, speeds):
    answer = []

    while progresses:
        progresses = [a + b for a, b in zip(progresses, speeds)]
        if progresses[0] >= 100:
            cnt = 1
            for i in range(1, len(progresses)):
                if progresses[i] < 100:
                    break
                cnt += 1
            answer.append(cnt)

            for i in range(cnt):
                progresses.pop(0)
                speeds.pop(0)

    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))