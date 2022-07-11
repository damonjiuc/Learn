n = 11
mas = ('3 ifepmjauwmbfxloivzpvh 7 lbexwmijsdehjzobbsyzqo -1 lrowbqbpeqlalbyois -1 jsuivhasegmfhyognwfbuqrdc 6 wcdnpyczovyobrbz 1 udrauyyzycttairwhoa -5 piiqghwazwevdeiulynyyks -5 pkklvcbaommegyuvxxwpxs -4 wiftexnuuwnonmfxeeaqak -4 pyhqaoixiylileyzjp -1 icziwuywktlpixvrzmycphcci')
splited = mas.split(' ')
k = []
s = []
for i in range(n):
    k.append(int(splited[i * 2]))
    s.append(splited[(i * 2) + 1])
for i in range(n):
    if k[i] > 0:
        first = s[i][k[i]:]
        second = s[i][0:k[i]]
    else:
        first = s[i][k[i]:]
        second = s[i][0:k[i]]
    print(first + second, end=' ')

