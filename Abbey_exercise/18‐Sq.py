n = 12
mas = ('42 9 21088 8 94 4 8180 11 2488 4 93114 8 3242 5 299 5 92 8 17695 12 23 9 83 6')
splited = mas.split(' ')
inted = []
for i in range(n * 2):
    inted.append(int(splited[i]))
for i in range(n):
    r = 1
    for u in range(inted[2 * i + 1]):
        r = (r + inted[2 * i] / r) / 2
    print(r, end=(' '))
