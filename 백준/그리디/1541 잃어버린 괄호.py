#https://www.acmicpc.net/problem/1541

sik = input()
result = 0
m_sik = sik.split('-')

if '-' not in sik:
    p_sik = sik.split('+')
    for i in p_sik:
        result += int(i)
else:
    for i in range(len(m_sik)):
        if i == 0:
            for j in m_sik[i].split('+'):
                result += int(j)
        else:
            p = 0
            for j in m_sik[i].split('+'):
                p += int(j)
            result -= p

print(result)
