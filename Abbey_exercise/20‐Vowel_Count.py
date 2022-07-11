n = 5
massive = ('+ 3 * 7 + 10 * 2 * 3 + 1 % 11')
splited = massive.split(' ')
count = int(len(splited) / 2 - 1)
for i in range(count):
    if splited[i * 2] == '+':
        n = n + int(splited[i * 2 + 1])
    if splited[i * 2] == '*':
        n = n * int(splited[i * 2 + 1])
n = n % int(splited[-1])
print(n)