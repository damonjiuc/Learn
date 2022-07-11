n = 3
massive = ('+ 7298 + 94 + 6032 * 4949 + 7 + 12 + 83 + 683 * 18 + 330 * 6 + 561 + 35 * 1 + 98 * 2061 + 10 * 20 * 1090 + 8375 + 688 * 9595 + 537 + 6507 + 5965 * 3176 + 248 * 51 + 3 * 5 + 100 * 1229 + 5511 + 1571 * 278 * 7 * 732 + 6099 + 6157 * 45 + 514 + 828 * 54 + 4 * 10 + 987 * 1818 + 9 + 8 + 183 * 471 + 820 % 7922')
splited = massive.split(' ')
count = int(len(splited) / 2 - 1)
for i in range(count):
    if splited[i * 2] == '+':
        n = n + int(splited[i * 2 + 1])
    if splited[i * 2] == '*':
        n = n * int(splited[i * 2 + 1])
n = n % int(splited[-1])
print(n)