n = 33
mas = ('75 2.10 72 2.27 43 1.98 62 1.54 68 1.62 82 2.61 51 1.37 109 1.79 108 2.68 61 2.02 76 2.33 92 2.48 49 1.24 116 2.30 104 1.80 79 1.52 115 1.76 92 2.04 118 2.17 65 1.58 95 2.60 101 2.14 81 2.25 91 1.77 83 2.63 103 2.62 109 1.97 114 2.76 69 1.38 110 1.77 69 1.60 70 2.09 117 2.31')
splited = mas.split(' ')
floated = []
for i in range(n * 2):
    floated.append(float(splited[i]))
for i in range(n):
    w = floated[i * 2]
    h = floated[(i * 2) + 1]
    bmi = w / (h ** 2)
    if bmi < 18.5:
        print('under', end=(' '))
    elif 18.5 <= bmi < 25.0:
        print('normal', end=(' '))
    elif 25.0 <= bmi < 30.0:
        print('over', end=(' '))
    elif bmi >= 30:
        print('obese', end=(' '))