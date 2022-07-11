n = 29
mas = ['SS SR PR SR RP RS SP PR SP SP', 'PR RR PS PP PP SP RP PR', 'RP PS SP PS PS PS SS PS', 'RS SP RR PP RS SR RS SS RP RS PR', 'RR PP RS RP RR PR RP SP', 'SR RR PS PP SP SR', 'PS PR RP RR SR SS RR PR RP', 'RR PR PP SR RS PR RS RS', 'PS RS SR PR RP', 'SP RR SR RS RR PR PS SP PP RS', 'PP SP PP PR PR PS PS SS SP PP PR', 'SR SP SS SP SR PR PP SR PS PS', 'PS SP PR PR PP RS PP SR PP PP SR PS SP PS PR', 'PS SS PS SP RP', 'SR RP RP', 'RS PP PS PS RS SS RP', 'RS RS RR PS SS SS PR PP SP SR PR RR PS PS SS PP RP RP', 'RS SP SR SR PR SP SR PS RR SR', 'SS SS PS RP PS RR SP SS SR PP PS RS RP', 'RS SS SP SR SR PR', 'SP PP RR RP PP RP RP RS RS PS SR RR PS', 'SS PP PP RR RP RS PP SR RR RS RS SP RS SS SS PR', 'SP PS SS SS PR PP SR PS', 'SS SR PR SR PP PP PS', 'SP SP PP SP SS PS PS SR RP RR SS RR SS PP PR RS', 'RR SR RR SP PP SP SR RP PS', 'RR RP PS PR PS PS', 'SP RS RS SR SR PR RP SS PR PR', 'PP RP PR RS SS RP SP RP RS RR RS SR PR']
first_wins = ['PR', 'RS', 'SP']
second_wins = ['RP', 'SR', 'PS']
for i in range(n):
    first = 0
    second = 0
    res = mas[i].split(' ')
    for i in range(len(res)):
        if res[i] in first_wins:
            first += 1
        elif res[i] in second_wins:
            second += 1
    if first > second:
        print('1', end=' ')
    elif second > first:
        print('2', end=' ')

