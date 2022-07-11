n = 21
mas = ('12 7 6 19 21 3 8 4 13 20 1 18 9 5 16 11 17 10 15 14 2')
splited = mas.split(' ')
inted = []
changed = 0
count = 0
change_check = -1
for i in range(n):
    inted.append(int(splited[i]))
while changed != change_check:
    change_check = changed
    for i in range(n - 1):
        if inted[i] > inted[i + 1]:
            inted[i], inted[i + 1] = inted[i + 1], inted[i]
            changed += 1
    count += 1
print(f'{count} {changed}')
