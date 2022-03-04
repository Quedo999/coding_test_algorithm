import time

# 내 풀이
n = list(map(int, input().split()))
m = list(map(int, input().split()))
cnt = 0
result = 0

s_time = time.time()

for i in range(len(m)-1):
    cnt += 1
    for x in range(cnt, len(m)):
        if m[i] == m[x]:
            continue
        result += 1

print(result)

e_time = time.time()

print(f'걸린 시간 : {e_time - s_time}')


## 답안
# n, m = map(int, input().split())
# data = list(map(int, input().split()))

# s_time = time.time()

# #1부터 10까지 무게를 담을 수 있는 리스트
# array = [0] * 11
# for x in data:
#     # 각 무게에 해당하는 볼링공의개수 카운트 
#     array[x] += 1

# result = 0
# # 1 부터 m까지의 각 무게에 대해 처리
# for i in range(1, m+1):
#     n -= array[i] # 무게가 i인 볼링공의 개수 (A가 선택할 수 있는 개수) 제외
#     result += array[i] * n # B가 선택하는 경우의 수와 곱하기

# print(result)

# e_time = time.time()

# print(f'걸린 시간 : {e_time - s_time}')