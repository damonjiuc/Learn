n = 4
mas = '7 1 199999 4'
inted = []
splited = mas.split(' ')
num = []
pn = [2]
u = 0
for i in range(n):
    inted.append(int(splited[i]))
for i in range(2, 1654321):
    num.append(i)
for i in range(1, len(num)):
    if num[i] % 2 != 0:
        pn.append(num[i])
while u < 300:
    i = 0
    check = pn[u + 1]
    while i + 2 < len(pn):
        if pn[i + 2] % check == 0:
            pn.pop(i + 2)
        else:
            i += 1
    u += 1
    
print(len(pn))
