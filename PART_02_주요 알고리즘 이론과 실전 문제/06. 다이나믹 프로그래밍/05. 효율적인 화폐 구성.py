n, m = map(int, input().split())
money_list = []

for _ in range(n):
    money_list.append(int(input()))

# 조건에 맞춰 dp테이블 초기화
d = [10001] * (m + 1)

# 0원으로 만들 수 있는건 0밖에 없기에 0으로 초기화
d[0] = 0

for i in range(n):
    for j in range(money_list[i], m+1):
        # (i - k)원을 만들 방법이 존재하는 경우
        if d[j - money_list[i]] != 10001:
            d[j] = min(d[j], d[j - money_list[i]] + 1)


if d[m] == 10001:
    print(-1)
else:
    print(d[m])
