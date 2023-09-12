from bisect import bisect_left, bisect_right

def solution(words):
    answer = 0
    words.sort()
    cnt = 0

    while words:
        cnt += 1
        w_list = [w[:cnt] for w in words]
        idx = 0

        while True:
            if idx == len(w_list) or not words:
                break
            l = bisect_left(w_list, w_list[idx])
            r = bisect_right(w_list, w_list[idx]) - 1
            if r - l == 0:
                answer += len(w_list[l])
                del w_list[idx]
                del words[idx]
            else:
                idx = r + 1

    return answer


words = ["word","war","warrior","world"]
print(solution(words))