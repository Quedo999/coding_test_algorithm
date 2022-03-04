n = int(input())
time_cnt = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                time_cnt += 1

print(time_cnt)