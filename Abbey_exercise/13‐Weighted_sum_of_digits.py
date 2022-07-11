n = 30
massive = ('27991697 320788 440307 3 1513 6 3 126307920 122623360 3 64999831 26 1729 159 63676176 31 51194367 1926 2 375797 76698809 104 3989557 343263 253935984 180366 14746 32682 4576 155422')
splited = massive.split(' ')
inted = []
for i in range(n):
    inted.append(int(splited[i]))
for i in range(n):
    x = inted[i]
    length = len(splited[i])
    sum = 0
    for u in range(length):
        ost = x % 10
        sum += ost * (length - u)
        x = x // 10
    print(sum, end=' ')


