def solution(N, number):
    d = dict()
    d[1] = {N}

    if N == number:
        return 1

    for i in range(2, 9):
        d[i] = {int(str(N)*i)}
        answer = 1
        while answer < i:
            temp = op(d[answer], d[i-answer])
            if number in temp:
                return i
            else:
                d[i].update(temp)
            answer += 1

        if number in d[answer]:
            return answer
    
    return -1

def op(a, b):
    temp = set()
    for i in a:
        for j in b:
            if i + j <= 32000:
                temp.add(i + j)
            if i - j >= 1:
                temp.add(i - j)
            if i * j <= 32000:
                temp.add(i * j)
            if i // j != 0:
                temp.add(i // j)
    return temp


N = 5
number = 12
print(solution(N,number))