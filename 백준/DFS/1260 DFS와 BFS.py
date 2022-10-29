# https://www.acmicpc.net/problem/1260

from collections import deque
import sys
input = sys.stdin.readline

n, m, start = list(map(int, input().split()))
m_list = [[] for _ in range(n+1)]
for i in range(m):
    a, b = list(map(int, input().split()))
    m_list[a].append(b)

chk = [False for _ in range(n+1)]


print(m_list)