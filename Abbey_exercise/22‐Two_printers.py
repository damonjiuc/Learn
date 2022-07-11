n = 18
mas = ('1033032 738826 668 286541741 186396711 3 3338 9950 98850 36180 62779 15518 1232709 7151763 89 74041254 50732039 8 117222 72036 4423 272 95 660082 634700 808262 543 2039407 619267 243 484 72 1731566 191 986 509697 838912 1077182 852 10432 15173 892 2 7 125209188 6833 2325 96361 5503 1585 78390 153 332 919186')
splited = mas.split(' ')
inted = []
for i in range(len(splited)):
    inted.append(int(splited[i]))
for i in range(n):
    a = inted[i * 3]
    b = inted[(i * 3) + 1]
    ntp = inted[(i * 3) + 2]
    count = 0
    printed = 0
    aprog = 0
    bprog = 0
    while printed < ntp:
        count += 1
        aprog += 1
        bprog += 1
        if aprog == a:
            printed += 1
            aprog = 0
        if bprog == b:
            printed += 1
            bprog = 0
    print(count, end=' ')