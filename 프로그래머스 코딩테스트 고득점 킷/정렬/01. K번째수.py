def solution(array, commands):
    answer = []

    for i, j, k in commands:
        n = array[i - 1 : j]
        n.sort()
        answer.append(n[k - 1])

    return answer


array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

print(solution(array, commands))
# return [5, 6, 3]