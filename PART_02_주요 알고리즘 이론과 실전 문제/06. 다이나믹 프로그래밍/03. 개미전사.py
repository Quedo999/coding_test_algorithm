n = int(input())
Map = list(map(int, input().split()))

d = [0] * 100
d[0] = Map[0]
d[1] = max(Map[0], Map[1])

for i in range(n):
    if i == 0 or i == 1:
        continue
    d[i] = max(d[i-1], d[i-2] + Map[i])

print(max(d))