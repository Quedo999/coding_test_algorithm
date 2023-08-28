# def solution(prices):
#     answer = []
#     for x in range(len(prices)):
#         cnt = 0
#         for y in prices[x+1:]:
#             cnt+=1
#             if prices[x] > y:
#                 break
#         answer.append(cnt)

#     return answer

def solution(prices):
    from collections import deque
    answer = []
    prices = deque(prices)
    while prices:
        p = prices.popleft()
        cnt = 0
        for i in prices:
            cnt += 1
            if p > i:
                break
        answer.append(cnt)
    return answer


prices = [1,2,3,2,3]
print(solution(prices))