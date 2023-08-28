"""
섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
"""

from heapq import heappush, heappop, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        a, b = heappop(scoville), heappop(scoville)
        heappush(scoville, a + (b * 2))
        answer += 1
    return answer

scoville, K = [1, 2, 12, 9, 3, 10], 7
print(solution(scoville, K))