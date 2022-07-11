n = 48
mas = '-32704553 9338 -75 -38442 1705 112510520 -167561 14644 -5 -250 52837731 -5706338 -700 11442923 1896074997 1621 43475805 -6025 2 -19 -3 122952403 10778278 508795940 1370839292 88652 -1 19451 693710570 -54951 615 -683695350 -42638 17459780 -903197 -14094 1537618 862085 154190 -1121 -159604549 -8231 1813 -563598 633210 -255 18 67416218'
inted = []
formated = []
splited = mas.split(' ')
for i in range(n):
    inted.append(int(splited[i]))
for i in range(n):
    formated.append('{:032b}'.format(inted[i]))
for i in range(n):
    num = str(formated[i])
    if num[0] == '-':
        num = num.replace('-', '0')
        num = num.replace('0', '2').replace('1', '3')
        num = num.replace('2', '1').replace('3', '0')
        num = bin(int(num, 2) + 1)
        num = str(num)[2:]
    count = 0
    for u in range(32):
        if num[u] == '1':
            count += 1
    print(count, end=' ')