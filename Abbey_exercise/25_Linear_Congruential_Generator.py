n = 16
mas = ('197 254180 47482 27515 24 83 12163 9256 6631 16 35 658656 5574 3699 16 1557 21873 82 53 6 1519 950 7 2 13 631 483160 23010 22428 14 157 58028 27 15 3 85 5 3426 3163 12 121 24 188629 21663 6 171 57 596704 3301 9 119 4200 291 223 15 163 9934 55 18 17 167 4013 738486 721430 6 621 98425 69474 66812 4 131 64 3 1 5 1275 7 1 0 9')
splited = mas.split(' ')
inted = []
for i in range(n * 5):
    inted.append(int(splited[i]))
for i in range(n):
    a = inted[i * 5]
    c = inted[(i * 5) + 1]
    m = inted[(i * 5) + 2]
    x0 = inted[(i * 5) + 3]
    num = inted[(i * 5) + 4]
    xcur = x0
    for i in range(num):
        xnext = (a * xcur + c) % m
        xcur = xnext
    print(xnext, end=' ')