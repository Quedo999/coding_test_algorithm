from heapq import heapify, heappop, heappush

def solution(numbers):
    answer = 0
    min_heap = numbers[:]
    max_heap = []
    heapify(min_heap)
    [heappush(max_heap, -n) for n in numbers]

    r = [[heappop(min_heap), -heappop(max_heap)] for _ in range(2)]
    return max([x*y for x,y in zip(*r)])

numbers = [1, 2, -3, 4, -5]
print(solution(numbers))