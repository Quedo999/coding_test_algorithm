# 점화식 : dp[i] = max(dp[i-1], dp[i-2] + dp[i])
# 집들이 원형으로 돼있기 때문에 처음과 끝이 만나는 연산은 하면 안됨
# 때문에 마지막이 빠진 리스트와 처음이 빠진 리스트로 나눠서 연산
# 마지막까지 돌고 각 리스트의 마지막원소를 비교해서 큰 값이 정답

def solution(money):
    # 분화된 리스트틀은 점화식을 고려해 앞에 원소 0을 하나 넣어둠.
    # 점화식에는 2번째 전 연산이 껴있기 때문
    s_money = [0] + money[:-1]
    e_money = [0] + money[1:]
    
    # 2번인덱스의 원소부터 탐색.
    for i in range(2, len(money)):
        s_money[i] = max(s_money[i-1], s_money[i] + s_money[i-2])
        e_money[i] = max(e_money[i-1], e_money[i] + e_money[i-2])
    
    # 다 돌았으면 마지막 원소들 끼리 비교

    return s_money[-1] if s_money[-1] > e_money[-1] else e_money[-1]


money = [1,2,3,1]
print(solution(money))