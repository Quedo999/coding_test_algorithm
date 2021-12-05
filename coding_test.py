def solution(drum):
  answer = -1

  dx = [1, 0, 0, 1]
  dy = [0, 1, -1, 0]
  move_type = ['#', '>', '<', '*']
  x = 0
  y = 0
  while y >= len(drum): 
    for move in range(len(move_type)):
      if drum[x][y] == move_type[move]:
        nx = x + dx[move]
        ny = y + dy[move]
  
  y += 1
  
  return answer


drum = ["######", ">#*###", "####*#", "#<#>>#", ">#*#*<", "######"]