import itertools

def solution(k, dungeons):
    answer = []
    dungeon_len = len(dungeons)

    for dungeon in itertools.permutations(dungeons):
        cnt = 0
        p = k
        for a, b in dungeon:
            if a <= p:
                p -= b
                cnt += 1
            else:
                answer.append(cnt)
                break
        if cnt == dungeon_len:
            answer.append(cnt)
            break

    return max(answer)

k = 80
dungeons = [[80,20],[50,40],[30,10]]

print(solution(k, dungeons))