def solution(arr):
    answer = [0, 0]
    quad(arr, [0, 0], len(arr), answer)
    return answer

def quad(arr, start_point, arr_range, answer):
    a, b = start_point
    num = arr[a][b]
    half_range = arr_range // 2
    for i in range(arr_range):
        for j in range(arr_range):
            if num != arr[a+i][b+j]:
                quad(arr, [a, b], half_range, answer)
                quad(arr, [a, b+half_range], half_range, answer)
                quad(arr, [a+half_range, b], half_range, answer)
                quad(arr, [a+half_range, b+half_range], half_range, answer)
                return
    answer[num] += 1

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))