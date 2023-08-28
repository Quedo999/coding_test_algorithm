"""
체크사항
1. 작업 하는 중 새로운 작업이 요청됐는가?
1-2. 작업 하는 중 새로운 작업들이 있다면 그 작업들의 작업 소요시간이 가장 작은것 부터 처리한다.
2. 작업이 끝날 때 까지 요청되지 않았는가?
"""

from heapq import heapify, heappop

def solution(jobs):
    heapify(jobs)
    
    job = heappop(jobs)
    jobTime = sum(job)
    result = [job[1]]
    
    while jobs:
        nextList = []
        if jobTime < jobs[0][0]:
            job = heappop(jobs)
            jobTime = sum(job)
            result.append(job[1])
            continue

        for _ in range(len(jobs)):
            if jobTime >= jobs[0][0]:
                nextList.append(heappop(jobs))
            else:
                break

        nextList = sorted(nextList, key=lambda x:x[1])
        nextTime, nextJobTime = nextList.pop(0)
        jobTime += nextJobTime
        result.append(jobTime - nextTime)
        jobs += nextList
        heapify(jobs)
          
    return sum(result) // len(result)

jobs = [[0, 10], [4, 10], [15, 2], [5, 11]]

print(solution(jobs))


"""
[[0, 3], [10, 1]] => 2
[[7, 8], [3, 5], [9, 6]] => 9
[[1, 4], [7, 9], [1000, 3]] => 5
[[0, 1], [2, 2], [2, 3]] => 2

"""