import re
from copy import deepcopy as dc
from collections import deque

def solution(user_id, banned_id):
    answer = set()
    banned_pattern = [re.compile(f"^{s.replace('*', '.')}$") for s in banned_id]
    match_ids_list = []
    for bp in banned_pattern:
        r = []
        for user in user_id:
            if re.match(bp, user):
                r.append(user)

        match_ids_list.append(r)

    q = deque()
    ban_len = len(banned_id)

    for start in match_ids_list[0]:
        q.append([start])
        while q:
            result = q.popleft()
            i = len(result)
            if i == ban_len:
                answer.add(tuple(sorted(result)))
                continue

            match_ids = match_ids_list[i]

            for match_id in match_ids:
                if match_id in result:
                    continue
                result.append(match_id)
                q.append(dc(result))
                result.pop()

    return len(answer)

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))