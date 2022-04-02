#coding test

# 화폐단위는 1, 5, 10, 50, 100, 500
def solution(money, costs):
    answer = 0
    coins = [1, 5, 10, 50, 100, 500]
    c_costs = []
    for i in range(6):
        c_costs.append([coins[i] / costs[i], coins[i], costs[i]])

    c_costs.sort(reverse=True)

    for i in c_costs:
        answer += (money // i[1]) * i[2]
        money %= i[1]
    return answer


money = 4578
costs = [1, 4, 99, 35, 50, 1000]

print(solution(money, costs))