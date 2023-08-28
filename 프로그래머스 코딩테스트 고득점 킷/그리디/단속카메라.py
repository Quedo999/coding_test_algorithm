def solution(routes):
    answer = 0
    routes = sorted(routes, key=lambda x:x[1])
    check_point = -1e9

    for in_point, out_point in routes:
        if check_point < in_point:
            check_point = out_point
            answer += 1

    return answer


routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))