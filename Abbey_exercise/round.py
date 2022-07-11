n = 35
massive = ('169 587 521 198 497 407 66 400 35 467 592 599 483 520 195 532 562 326 275 246 175 448 316 432 267 432 512 290 36 278 140 403 219 486 313')
splited = massive.split(' ')
f = []
for i in range(n):
    f.append(int(splited[i]))
for i in range(n):
    c = (f[i] - 32) * 5 // 9
    if (f[i] - 32) * 5 % 9 >= 4.5:
        print(c+1, end=' ')
    else:
        print(c, end=' ')
