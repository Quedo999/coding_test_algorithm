def solution(numbers):
    answer = ''.join(sorted([str(i) for i in numbers], key=lambda x:x*4 ,reverse=True)).lstrip('0')
    
    return '0' if answer == '' else answer




# # 테스트 케이스 1
# numbers = [6, 10, 2]
# # return : 6210

# 테스트 케이스 2
numbers = [3, 30, 34, 5, 9]
# return : 9534330

print(solution(numbers))