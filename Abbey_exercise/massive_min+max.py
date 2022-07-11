n = 31
a = []
b = []
massive = ('17587 478 -9098136 4183537 37 2 10029 644 54 4 31 2 4099 1482 1641972 285 21 14 164 8 7370501 228355 12553 1268 18455 802 45 10 76 8 9 6 -565511 1841946 62 4 1343311 985 -2539060 4741488 2042774 988 18241 1052 3232315 68 1139343 104 5200747 889390 2715313 -4858562 -4659573 1122881 16891 1494 -1093869 1898577 6193418 58 9 6')
splited = massive.split(' ')
for i in range(0, len(splited), 2):
    a.append(splited[i])
for i in range(1, len(splited), 2):
    b.append(splited[i])
for i in range(n):
    c = int(a[i]) // int(b[i])
    if c > 0:
        if int(a[i]) % int(b[i]) / int(b[i]) >= 0.5:
            print(c+1, end=' ')
        else:
            print(c, end=' ')
    else:
        if int(a[i]) % int(b[i]) / abs(int(b[i])) >= 0.5:
            print(c+1, end=' ')
        else:
            print(c, end=' ')