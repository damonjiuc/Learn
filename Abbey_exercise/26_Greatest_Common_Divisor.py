n = 22
mas = ('4030 4745 2665 1968 510 9647 170 7 7 8 97 36 9688 9 2619 2646 204 8 7 6 8835 1116 6384 6132 920 713 63 755 4278 8 51 55 4 352 7050 7500 864 3024 1386 2640 6780 7 1 2')
splited = mas.split(' ')
inted = []
a = []
b = []
for i in range(n * 2):
    inted.append(int(splited[i]))
for i in range(n):
    a.append(inted[i * 2])
    b.append(inted[(i * 2) +1])
for i in range(n):
    if a[i] < b[i]:
        min = a[i]
        gcd = b[i]
    else:
        min = b[i]
        gcd = a[i]
    while min != gcd:
        while min < gcd:
            gcd = gcd - min
        min, gcd = gcd, min
    lcm = int(a[i] * b[i] / gcd)
    print(f'({gcd} {lcm})', end=' ')
