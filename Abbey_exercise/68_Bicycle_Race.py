n = 26
mas = ('234 11 10 28 14 10 114 15 22 16 25 21 26 20 21 39 18 16 11 23 13 12 24 24 29 14 20 103 13 14 88 17 26 40 14 28 30 25 10 58 21 14 238 13 14 173 17 30 183 18 17 16 19 12 75 10 17 53 17 14 464 30 26 14 14 21 104 14 25 13 19 10 26 19 25 195 30 17')
splited = mas.split(' ')
inted = []
for i in range(n * 3):
    inted.append(int(splited[i]))
for i in range(n):
    s = inted[i * 3]
    first = inted[(i * 3) + 1]
    second = inted[(i * 3) + 2]
    rez = s / (first + second) * first
    if rez % 1 == 0:
        print(int(rez), end=' ')
    else:
        print(rez, end=' ')