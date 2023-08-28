import math

def solution(brown, yellow):
    if yellow == 1:
        w = int(math.sqrt(brown + yellow))
        return [w, w]
    half = yellow // 2

    for h in range(1, half + 1):
        if yellow % h != 0:
            continue
        
        w = yellow // h
        areaW = w + 2
        areaH = h + 2
        area = areaW * areaH
        if area - yellow == brown:
            return [areaW, areaH]

brown, yellow = 8, 1

print(solution(brown, yellow))