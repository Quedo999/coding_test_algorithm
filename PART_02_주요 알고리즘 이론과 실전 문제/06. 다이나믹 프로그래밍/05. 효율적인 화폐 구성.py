# 226 page

# n개의 줄에 각 화폐의 가치가 주어짐. 화폐 가치는 10000보다 작거나 같은 자연수
n, m = map(int, input().split())
money_list = []
d = [10001] * (m + 1) # 화폐가치 최대가 10000이므로 10001은 불가능 하다는 의미

d[0] = 0

for _ in range(n):
    money_list.append(int(input()))
money_list.sort()

for i in range(n):
    for j in range(money_list[i], m + 1):
        if d[j - money_list[i]] != 10001: # (i - k) 원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - money_list[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])