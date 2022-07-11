n = 13
massive = ('285 81 87 103 221 58 74 178 141 58 68 142 200 272 127 264 172 134 147 109 66 309 149 157 136 128 52 340 256 12 220 124 186 281 62 148 156 273 192')
splited = massive.split(' ')
a = []
b = []
c = []
for i in range(0, n*3, 3):
    a.append(int(splited[i]))
for i in range(1, n*3, 3):
    b.append(int(splited[i]))
for i in range(2, n*3, 3):
    c.append(int(splited[i]))
for i in range(n):
    s = a[i] * b[i] + c[i]
    res = 0
    for u in range(len(str(s))):
        r = s % 10
        s = s // 10
        res += r
        print(res)
    print(res, end=' ')
