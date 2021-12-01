# 201 page
'''
 전형적인 이진탐색, 파라메트릭 서치 유형의 문제.
파라메트릭 서치 : 최적화 문제를 결정 문제로 바꿔 해결하는 기법
결정 문제 : '예', 혹은'아니오' 로 답하는 문제
'원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 파라메트릭 서치를 이용.
코딩테스트나 프로그래밍 대회에서 보통 파라메트릭 서치 유형은 이진 탐색을 이용해 해결함.
'''

n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0

while(start<=end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
       end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답 이므로, 여기서 result에 기록
        start = mid + 1

# 정답 출력
print(result)