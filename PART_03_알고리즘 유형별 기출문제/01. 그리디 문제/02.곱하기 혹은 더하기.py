numbers = input()
result = int(numbers[0])

for i in range(1, len(numbers)):
  number = int(numbers[i])
  result = max(result + number, result * number)

print(result)