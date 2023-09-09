def solution(m, n, puddles):
    f = int(1e9+7)
    h_map = [[0]*(m+1) for _ in range(n+1)]
    h_map[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles or [i, j] == [1, 1]:
                continue
            else:
                h_map[i][j] = h_map[i][j-1] + h_map[i-1][j]
                

    return h_map[n][m] % f


m, n = 4, 3
puddles = [[2,2]]
print(solution(m, n, puddles))