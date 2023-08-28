def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if i + 1 > citations[i]:
            return i
    
    return len(citations)


citations = [3, 0, 6, 1, 5]
print(solution(citations))