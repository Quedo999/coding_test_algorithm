# triangle 리스트를 뒤에서부터 정점을 향해 탐색.
# n과 n+1을 비교해서 큰 것을 아래 n에 더함
# 최종적으로 정점까지 더하면 최댓값이 출력됨

def solution(triangle):
    for i in range(len(triangle)-1,-1,-1):
        t = triangle[i]
        for j in range(len(t)-1):
            if t[j] >= t[j+1]:
                triangle[i-1][j] += t[j]
            else:
                triangle[i-1][j] += t[j+1]
      
    return triangle[0][0]


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))