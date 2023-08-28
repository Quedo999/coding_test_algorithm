from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [False for _ in range(len(words))]
    
    q = deque([[begin, 0]])
    while q:
        change_word, change_cnt = q.popleft()
        if change_word == target:
            return change_cnt
        for w_idx, word in enumerate(words):
            cnt = 0
            for i, c_word in enumerate(change_word):
                if word[i] != c_word:
                    cnt += 1
                    if cnt > 1:
                        continue
            if cnt == 1 and not visited[w_idx]:
                visited[w_idx] = True
                q.append([word, change_cnt + 1])

    return answer


begin = "hit"
target = "cog"

words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin, target, words))