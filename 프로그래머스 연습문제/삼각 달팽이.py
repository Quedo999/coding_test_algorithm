def solution(n):
    answer = []
    triangle = [[0] * i for i in range(1, n + 1)]
    num = 0
    cnt, i, j = n, -1, 0
    d = [[1, 0], [0, 1], [-1, -1]]
    d_switch = 0

    while cnt != 0:
        for _ in range(cnt):
            num += 1
            i += d[d_switch][0]
            j += d[d_switch][1]
            triangle[i][j] = num

        cnt -= 1

        if d_switch == 2:
            d_switch = 0
        else:
            d_switch += 1

    for i in triangle:
        for j in i:
            answer.append(j)
    return answer


n = 5
print(solution(n))