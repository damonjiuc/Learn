n = 20
mas = ('25 532 2293 2004 3217 149 35 18 130 1778 61 36524 47 1142 468 23 2159 35 19468 38173')
splited = mas.split(' ')
inted = []
for i in range(n):
    inted.append(int(splited[i]))
for i in range(n):
    x = inted[i]
    count = 0
    while x != 1:
        if x % 2 == 0:
            x = x / 2
            count += 1
        else:
            x = 3 * x + 1
            count += 1
    print(count, end=(' '))