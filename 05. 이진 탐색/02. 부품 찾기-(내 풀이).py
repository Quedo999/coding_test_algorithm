# 197 page

import sys

n = int(input())
array = set(map(int, sys.stdin.readline().rstrip().split()))

m = int(input())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))

for i in m_list:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')