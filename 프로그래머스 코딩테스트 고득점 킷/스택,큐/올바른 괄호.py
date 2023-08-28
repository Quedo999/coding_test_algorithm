"""
맨 처음 시작이 ) 이거나 마지막이 ( 라면 바로 false 리턴
각 괄호의 갯수가 서로 맞지 않으면 바로 false 리턴
"""

def solution(s):
    # if s.count('(') != s.count(')') or s.startswith(')') or s.endswith('('):
    #     return False
    
    # return True
    if s.startswith(')') or s.endswith('('):
        return False

    stack = []

    for bracket in s:
        stack.append(bracket)
        if len(stack) > 1 and stack[-1] == ')' and stack[-2] == '(':
            stack.pop()
            stack.pop()
    
    if stack:
        return False
    return True


s="()()"

print(solution(s))