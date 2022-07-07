n = int(input())
array = list(map(int, input().split()))
array.sort()

group = 0
cnt = 0
for i in array:
  cnt += 1
  if cnt == i:
    group += 1
    cnt = 0

print(group)