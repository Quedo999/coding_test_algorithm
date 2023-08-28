from heapq import heapify, heappop, heappush

def solution(operations):
    heap = []
    for o in operations:
        if o[0] == 'I':
            heap = addheap(heap, int(o.split()[1]))
        elif o[:3] == 'D 1':
            heap = delMax(heap)
        elif o[:3] == 'D -':
            heap = delMin(heap)
    
    if not heap:
        return [0,0]
    
    return [max(heap), min(heap)]

def addheap(heap, value):
    heappush(heap, value)
    return heap

def delMax(heap):
    if not heap:
        return []
    maxHeap = [-i for i in heap]
    heapify(maxHeap)
    heappop(maxHeap)
    maxHeap = [-i for i in maxHeap]
    heapify(maxHeap)
    return maxHeap

def delMin(heap):
    if not heap:
        return []
    heappop(heap)
    return heap


operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]

print(solution(operations))