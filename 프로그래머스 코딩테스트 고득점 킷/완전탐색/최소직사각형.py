"""
가로 세로중 큰 값을 가로, 작은값을 세로로 둠
그 중 가장 큰 값의 가로 * 가작 큰 값의 세로
"""

def solution(sizes):
    w = []
    h =[]

    for a, b in sizes:
        if a >= b:
            w.append(a)
            h.append(b)
        else:
            w.append(b)
            h.append(a)
    
    return max(w) * max(h)

sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
print(solution(sizes))