n = 16
mas = ('312012 208886 2479 36516557 19438608 21 1162037 1066888 333 2934343 8753020 94 31991909 9441212 10 1 1 603227996 46355 16731 12350 1 1 834061976 89768 128312 3913 93616936 59602815 8 196572 151591 3435 19735349 15057901 25 134744420 64348636 4 3566730 5853872 157 1 1 768621874 85023 73166 8078')
splited = mas.split(' ')
inted = []
for i in range(len(splited)):
    inted.append(int(splited[i]))
for i in range(n):
    x = inted[i * 3]
    y = inted[(i * 3) + 1]
    s = inted[(i * 3) + 2]
    sx = int(s * y / (x + y))
    first = (s - sx) * y
    second = (sx + 1) * x
    if first < second:
        time = int(first)
    else:
        time = int(second)
    print(time, end=' ')