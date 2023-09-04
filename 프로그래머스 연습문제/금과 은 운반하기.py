def solution(a, b, g, s, w, t):
    answer = -1
    right = max(t) * 2 * (a+b)
    left = min(t)
    citys = len(g)

    while left <= right:
        # mid: 옮길 시간, 해당 시간에 옮길 수 있는 총 금은 무게, 금무게, 은무게 변수 초기화
        mid = (right + left) // 2
        acc_gold_silver = 0
        acc_gold = 0
        acc_silver = 0
        for i in range(citys):
            # 시간 안에 옮길 수 있는 횟수
            cnt = mid // (2 * t[i])
            if  mid % (2 * t[i]) >= t[i]: cnt += 1

            # 시간안에 옮길 수 있는 무게
            weight = min(cnt * w[i], g[i] + s[i])
            acc_gold_silver += weight
            acc_gold += min(weight, g[i])
            acc_silver += min(weight, s[i])
        if acc_gold_silver >= a + b and acc_gold >= a and acc_silver >= b:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer

a, b, g, s, w, t = 90, 500, [70,70,0], [0,0,500], [100,100,2], [4,8,1]
print(solution(a, b, g, s, w, t))