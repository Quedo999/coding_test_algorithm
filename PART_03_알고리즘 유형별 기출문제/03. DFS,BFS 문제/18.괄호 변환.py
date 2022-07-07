# 균형잡힌 문자열 판단
def sol_a(p):
    a, b = 0, 0
    for i in p:
        if i == "(":
            a += 1
        else:
            b += 1
        if a == b:
            return a + b

# 올바른 문자열 판단
def sol_b(p):
    cnt = 0
    for i in p:
        if i == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            else:
                cnt -= 1
    return True


def solution(p):
    answer = ''

    if p == '':
        return p

    u = p[:sol_a(p)]
    v = p[sol_a(p):]

    # u가 균형잡힌 문자열이면 v를 1단계부터 시작
    if sol_b(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for x in range(len(u)):
            if u[x] == "(":
                u[x] = ")"
            else:
                u[x] = "("
        answer += ''.join(u)
    return answer

print(solution("()))((()"))