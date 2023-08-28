def solution(arr):
    answer = [arr[i] for i in range(len(arr)) if i == 0 or arr[i] != arr[i-1]]
    
    return answer

arr = [1,1,3,3,0,1,1]
print(solution(arr))