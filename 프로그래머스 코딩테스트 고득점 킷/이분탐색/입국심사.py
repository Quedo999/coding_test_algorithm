def solution(n, times):
    left = min(times)
    right = min(times) * n

    while left <= right:
        mid = (right + left ) // 2
        checkPerson = 0
        for time in times:
            checkPerson += mid // time
            if checkPerson >= n:
                break
        
        if checkPerson >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer


n = 6
times = [7,10]
print(solution(n, times))