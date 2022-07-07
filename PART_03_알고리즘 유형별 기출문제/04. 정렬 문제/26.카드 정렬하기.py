n = int(input())
ls = [int(input()) for _ in range(n)]

ls.sort()

t_ls = []
for i in range(1, len(ls)):
    if i == 1:
        t_ls.append(ls[i-1] + ls[i])
    else:
        t_ls.append(t_ls[i-2] + ls[i])

print(sum(t_ls))