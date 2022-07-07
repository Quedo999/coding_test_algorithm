#https://programmers.co.kr/learn/courses/30/lessons/60057

def solutions(s):
    result = len(s)

    # 압축 범위를 늘려감
    for i in range(1, len(s) // 2 + 1):
        compressed = ''
        point = s[0:i]
        cnt = 1
        # 범위만큼 이동하며 이전 문자열과 비교
        for j in range(i, len(s), i):
            # 같은 문자열이면 cnt 증가
            if point == s[j:j+i]:
                cnt += 1
            # 아니면 문자열 등록시키고 넘어감
            else:
                compressed += str(cnt) + point if cnt >= 2 else point  # 삼항연산. cnt가 2 이상이면 카운트 + 문자열, 아니라면 그냥 문자열만 입력
                point = s[j:j+i] # point를 다음 비교할 문자열로 변경
                cnt = 1 # cnt역시 초기화
        # 남은 문자열 처리
        compressed += str(cnt) + point if cnt >= 2 else point
        # 만들어지는 압축 문자열이 가장 짧은 것 비교
        result = min(result, len(compressed))

    return result



print(solutions('aabbaccc'))