n = 17
mas = ('290 502 40 349 606 405 190 85 455 560 130 785 743 230 692 844 649')
splited = mas.split(' ')
inted = []
index = []
changed = 0
change_check = -1
for i in range(n):
    inted.append(int(splited[i]))
    index.append(i + 1)
while changed != change_check:
    change_check = changed
    for i in range(n - 1):
        if inted[i] > inted[i + 1]:
            inted[i], inted[i + 1] = inted[i + 1], inted[i]
            index[i], index[i + 1] = index[i + 1], index[i]
            changed += 1
print(*index)
