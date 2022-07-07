# 내 풀이 : 표준 라이브러리인 bisect 이용함.
from bisect import bisect_left, bisect_right

n, x = map(int, input().split())

n_list = list(map(int, input().split()))

result = bisect_right(n_list, x) - bisect_left(n_list, x)

if result == 0:
    print(-1)
else:
    print(result)

