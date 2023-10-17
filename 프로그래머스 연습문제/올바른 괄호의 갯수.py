from collections import defaultdict

def solution(n):
    d = defaultdict(int)
    d[0] = 1
    
    def c(n):
        l = []
        for i in range(n):
            if not d[n-1-i]:
                c(n-1-i)
            l.append(d[i]*d[n-1-i])
        d[n] = sum(l)
    c(n)
    
    return d[n]


n = 5
print(solution(n))