from collections import defaultdict

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    ban_dict = defaultdict(set)

    for r in report:
        report_id, ban_id = r.split()
        ban_dict[ban_id].add(report_id)
        
    for report in ban_dict.values():
        if len(report) < k:
            continue
        for r in report:
            answer[id_list.index(r)] += 1

    return answer



id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))