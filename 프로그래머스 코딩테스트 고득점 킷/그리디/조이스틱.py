def solution(name):
    answer = 0
    # 모두 A라면 0 반환
    if set(name) == {'A'}:
        return 0
    
    # 상하조작 횟수
    for i in name:
        if ord(i) <= 78:
            answer += ord(i) - 65
        else:
            answer += 90 - ord(i) + 1
    
    # 좌우조작 횟수
    # 최대로 움직일 수 있는 횟수. 한 뱡향으로만 쭉 갔을 때
    max_times = len(name) - 1
    cnt_results = [max_times]

    # A가 없으면
    if 'A' not in name:
        return answer + max_times

    # 문자열 변경해가며 좌우조작횟수 구하기
    for i in range(len(name) // 2 + 1):
        a = name[-i:] + name[:-i]
        b = name[i::-1] + name[i+1:][::-1]
        for n in [a, b]:
            for _ in range(len(n)):
                if n[-1] != 'A':
                    break
                n = n[:-1]
            if len(n) + i - 1 >= max_times:
                continue
            cnt_results.append(len(n) + i - 1)
    
    return answer + min(cnt_results)


name = "BBBABBB"
print(solution(name))