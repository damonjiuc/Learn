n = 13
mas = '5846 7748 5461 4890 3936 7807 7478 614 9501 430 8504 571 8611 6074 1694 8008 3544 1023 435 4768 2539 4458 507 7571 3723 6909 8586 4907 8257 5818 6848 6511 7246 9410 5225 1112 7056 7276 3010 9686 7693 6589 1732 4473 7235 2704 9521 2209 5266 1571 396 5027 6053 3899 9483 4864 199 7336 158 2628 4549 5578 1442 239 5278 6557 166 8515 5519 4897 8942 4851 6142 9166 9350 1965 4693 2855'
splited = mas.split(' ')
inted = []
for i in range(n * 6):
    inted.append(int(splited[i]))
def sides(xa, ya, xb, yb):
    if xa >= xb:
        if ya >= yb:
            side = ((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5
        elif yb >= ya:
            side = ((xa - xb) ** 2 + (yb - ya) ** 2) ** 0.5
    elif xb >= xa:
        if ya >= yb:
            side = ((xb - xa) ** 2 + (ya - yb) ** 2) ** 0.5
        elif yb >= ya:
            side = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
    return side
for i in range(n):
    x1 = inted[i * 6]
    y1 = inted[(i * 6) + 1]
    x2 = inted[(i * 6) + 2]
    y2 = inted[(i * 6) + 3]
    x3 = inted[(i * 6) + 4]
    y3 = inted[(i * 6) + 5]
    a = sides(x1, y1 , x2 , y2)
    b = sides(x2, y2, x3, y3)
    c = sides(x3, y3, x1, y1)
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    s = round(s, 7)
    if s % 1 == 0:
        s = int(s)
    print(s, end=' ')
