st = input()
alpha = []
number = 0
for i in st:
    if i.isalpha():
        alpha.append(i)
    else:
      number += int(i)

alpha.sort()

if number != 0:
    print(''.join(alpha) + str(number))
else:
    print(''.join(alpha))