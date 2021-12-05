data = input()

zero_cnt = 0
one_cnt = 0

if data[0] == '1':
  one_cnt = 1
else:
  zero_cnt = 1

for i in range(1, len(data)):
  if data[i] == data[i - 1]:
    continue
  else:
    if data[i - 1] == '1':
      one_cnt += 1
    else:
      zero_cnt += 1

print(min(zero_cnt, one_cnt))