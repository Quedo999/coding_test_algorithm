# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3

# 풀이
def solution(n, lost, reserve):
    answer = 0
    stu_list = [i+1 for i in range(n)]
    reserve.sort()
    lost.sort()

    rm_list = []

    for i in reserve:
        if i in lost:
            rm_list.append(i)

    for i in rm_list:
        reserve.remove(i)
        lost.remove(i)

    for i in stu_list:
        if i in lost:
            if i - 1 in reserve:
                reserve.remove(i - 1)
                pass
            elif i + 1 in reserve:
                reserve.remove(i + 1)
                pass
            else:
                continue
        answer += 1

    return answer