n = 28
mas = ('295 513 462 30 7 8 1 82 77 126 143 51 519 24 616 116 74 72 5 15 21 471 508 570 797 50 4 680 1031 1122 75 172 677 179 128 59 151 44 115 97 281 4 574 31 11 542 12 466 917 1 32 854 847 940 73 1 8 4 7 24 275 2 6 85 79 20 540 545 136 77 134 131 97 193 160 286 28 981 100 2 459 3 768 9')
splited = mas.split(' ')
inted = []
for i in range(n * 3):
    inted.append(int(splited[i]))
a = []
b = []
c = []
for i in range(n):
    a = inted[i * 3]
    b = inted[(i * 3) + 1]
    c = inted[(i * 3) + 2]
    if a < b < c:
        print(b, end=(' '))
    if a < c < b:
        print(c, end=(' '))
    if b < a < c:
        print(a, end=(' '))
    if b < c < a:
        print(c, end=(' '))
    if c < b < a:
        print(b, end=(' '))
    if c < a < b:
        print(a, end=(' '))