n = 12
mas = ('6239 3251 3384 1687 770 6068 2968 7457 6363 3488 779 8206')
splited = mas.split(' ')
inted = []
for i in range(n):
    inted.append(int(splited[i]))
for i in range(n):
    used = []
    a = inted[i]
    used.append(a)
    count = 0
    ch = False
    while not ch:
        count += 1
        rand = a * a
        rand = int(str(rand).zfill(8))
        rand = (rand // 100) % 10000
        if rand in used:
            ch = True
        else:
            used.append(rand)
            a = rand
    print(count, end=' ')