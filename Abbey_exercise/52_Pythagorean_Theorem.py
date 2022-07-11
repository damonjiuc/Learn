n = 25
mas = ('150 360 390 324 135 345 357 1224 1313 708 295 760 235 564 611 648 189 690 540 288 676 80 192 220 356 267 491 152 114 160 960 400 1080 1272 371 1293 240 320 400 240 100 277 328 615 697 840 245 852 705 376 891 585 312 663 630 336 706 328 615 697 198 264 377 1008 420 1140 15 20 21 175 600 647 384 720 815')
splited = mas.split(' ')
inted = []
for i in range(n * 3):
    inted.append(int(splited[i]))
for i in range(n):
    a = inted[i * 3]
    b = inted[(i * 3) + 1]
    c = inted[(i * 3) + 2]
    sqrt = int(((a ** 2) + (b ** 2)) ** 0.5)
    if c == sqrt:
        print('R', end=' ')
    elif c < sqrt:
        print('A', end=' ')
    elif c > sqrt:
        print('O', end=' ')