import math

def solution(n, clockwise):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    answer[0][0] = 1

    #방향 지정, 오 밑 왼 위
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    if clockwise:
        r = math.ceil(n/2)
        m_point = [[0,0], [0, n-1], [n-1,n-1],[n-1,0]]
        for m in m_point:
            i, j = m[0], m[1]
            tmp = n - 1
            cnt = 0
            while n - r != tmp:
                for _ in range(tmp):
                    cnt += 1
                    answer[i][j] = cnt
                break

    return answer

n = 5
clockwise=True
print(solution(n, clockwise))