n = 3   
massive = ('1 0 0 0 2 3 4 5 5 3 23 22 24 4 20 45 8 4 6 47 9 11 51 13')
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
    print(f'({d} {h} {m} {s})')