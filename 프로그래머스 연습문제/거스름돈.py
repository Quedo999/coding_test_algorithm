# n+1만큼의 인덱스를 가진 DP테이블 생성 ex) n=5 이면 마지막 인덱스는 5가 됨
# 각 인덱스 번호는 가지고 있는 돈으로 만들 수 있는 돈. 인덱스가 3이면 3원을 만들 수 있는 경우의 수가 됨
# money를 돌며 DP 테이블을 업데이트시킴
# 해당 DP 테이블을 업데이트 시킬 점화식
# dp[i] += dp[i-money]
# 해당 계산을 하기위해 dp테이블의 0번인덱스의 값은 1로 초기화
# dp테이블의 마지막원소를 문제에서 제시하는 값으로 나눈 게 정답이 됨

def solution(n, money):
    dp = [0 for _ in range(n+1)]
    dp[0] = 1
    INF = int(1e9) + 7

    for m in money:
        # 현재 money 보다 작은 값은 만들지 못하므로 m부터 시작.
        # ex) money가 2원이면 1원은 만들수 없음 
        for i in range(m, n+1):
            dp[i] += dp[i-m]

    return dp[-1] % INF


n = 5
money = [1,2,5]
print(solution(n, money))