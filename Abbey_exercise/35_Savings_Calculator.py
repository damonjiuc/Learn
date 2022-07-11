n = 17
mas = ('10000 180000 7 500 4500 50 1000 4000 6 50 550 45 500 7500 3 250 1000 7 1000 5000 6 500 4000 40 25 250 4 25 375 2 10000 200000 3 100 1300 45 100 1300 35 500 12500 3 1000 3000 10 250 3250 35 250 2500 1')
splited = mas.split(' ')
inted = []
for i in range(n * 3):
    inted.append(int(splited[i]))
for i in range(n):
    start = inted[i * 3]
    finish = inted[(i * 3) + 1]
    p = inted[(i * 3) + 2]
    current = start
    years = 0
    while current < finish:
        current = current + current * p / 100
        current = current - current * 100 % 1 / 100
        years += 1
    print(years, end=' ')
