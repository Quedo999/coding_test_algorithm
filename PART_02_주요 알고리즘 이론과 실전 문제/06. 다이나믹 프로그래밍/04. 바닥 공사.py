# 223 page
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍 진행
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i - 1] + 2 * d[i-2])
print(d[n])