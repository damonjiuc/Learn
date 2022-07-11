n = 10
massive = ('19 14 50 19 20 15 40 10 11 20 30 45 21 7 20 24 23 12 41 5 29 16 24 15 1 10 11 23 21 14 30 0 11 5 33 49 12 23 31 44 5 16 0 16 13 18 19 54 10 18 44 4 23 3 9 12 9 5 16 52 10 18 21 56 16 2 17 34 16 12 59 55 7 4 23 36 10 0 28 54')
splited = massive.split(' ')
d1 = []
h1 = []
m1 = []
s1 = []
d2 = []
h2 = []
m2 = []
s2 = []
for i in range(0, n*8, 8):
    d1.append(int(splited[i]))
for i in range(1, n*8, 8):
    h1.append(int(splited[i]))
for i in range(2, n*8, 8):
    m1.append(int(splited[i]))
for i in range(3, n*8, 8):
    s1.append(int(splited[i]))
for i in range(4, n*8, 8):
    d2.append(int(splited[i]))
for i in range(5, n*8, 8):
    h2.append(int(splited[i]))
for i in range(6, n*8, 8):
    m2.append(int(splited[i]))
for i in range(7, n*8, 8):
    s2.append(int(splited[i]))
for i in range(n):
    o = s1[i] + m1[i] * 60 + h1[i] * 3600 + d1[i] * 3600 * 24
    p = s2[i] + m2[i] * 60 + h2[i] * 3600 + d2[i] * 3600 * 24
    s = (p - o) % 60
    m = (p - o) // 60 % 60
    h = (p - o) // 60 // 60 % 24
    d = (p - o) // 60 // 60 // 24
    print(f'({d} {h} {m} {s})', end=' ')