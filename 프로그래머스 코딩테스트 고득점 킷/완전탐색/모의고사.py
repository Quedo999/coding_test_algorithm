"""
1 : 1,2,3,4,5
2 : 2,1,2,3,2,4,2,5,2,1
3 : 3,3,1,1,2,2,4,4,5,5
"""

def solution(answers):
    answer = []
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    one *= len(answers) // len(one) + 1
    two *= len(answers) // len(two) + 1
    three *= len(answers) // len(three) + 1

    oneCnt, twoCnt, threeCnt = 0, 0, 0

    for i, v in enumerate(answers):
        if one[i] == v:
            oneCnt += 1
        if two[i] == v:
            twoCnt += 1
        if three[i] == v:
            threeCnt += 1
    
    result = [oneCnt, twoCnt, threeCnt]
    maxCnt = max(result)

    for i, v in enumerate(result):
        if v == maxCnt:
            answer.append(i+1)
    
    return answer

answers = [1,3,2,4,2]

print(solution(answers))
