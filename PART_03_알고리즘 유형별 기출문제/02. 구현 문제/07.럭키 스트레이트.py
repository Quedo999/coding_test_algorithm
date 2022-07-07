a = input()
l = 0
r = 0


for i in range(len(a)):
  if i < ((len(a) // 2)):
    l += int(a[i])
  else:
    r += int(a[i])

if l == r:
  print('LUCKY')
else:
  print('READY')