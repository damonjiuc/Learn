n = 20
inp = ['H Hczm mss Aabszyt, Tyz-Sh, A-Assmmzch, H',
'Etlrvzugvcigokg-icvg, uzvrlte',
'Znyvuaee ey, hbb-H, yee-Eauvynz',
'Iycti, lah iio a, l-it-cyi',
'Atuorjoceywuacahik-smosyysomskihacauwy-ecojroyta',
'Nn T-Ouvb, huewawe, Uhbu, ot N N',
'Ctwugyeqk, wvgeoxtetxoegvwkqeyguwtc',
'Fj-jyjuzqwwoy-tyuruvuruy Ty, o wwqz, Ujyjjf',
'Cm Edtxawineptudeofd ayj ojy, Adfo-e dutpeniwa Xtd, emc',
'KqtouGd, N i, n dgo T, qk',
'Ycyqjfupposowrouvotqgukllkugqtovuorw-osoppufjqyc y',
'Goq-l lmdaooa-dmllqog',
'Zh-J cueiewsub, Z-Y eiojaeeajoieyz-Bus, Weieucjhz',
'Cyjxf Uveoqyyyyqo-Evufxjyc',
'YobiLcsv xieol Viv, Loeix-V-sc-lboy',
'Yo, Vo, Iy Sisyi, Ovoy',
'Aeunibytw, p-Yeilibiouoibiliey, P-Wtybinuea',
'Ouuile, x, eliu, Uo',
'Etjm Mu-anoifik-uf, Sfu, ki, Fi-ona umejte',
'Uxmfunhp Eo, Y, Yaephnu fmxu']
def checker(inp_str):
    inp_str = inp_str.split(',')
    inp_str = ''.join(inp_str)
    inp_str = inp_str.split('!')
    inp_str = ''.join(inp_str)
    inp_str = inp_str.split(' ')
    inp_str = ''.join(inp_str)
    inp_str = inp_str.split('-')
    inp_str = ''.join(inp_str)
    opt_str = inp_str.lower()
    
    check = 'Y'
    i = 0
    while i <= int(len(opt_str) / 2):
        if opt_str[i] != opt_str[-i - 1]:
            check = 'N'
        i += 1
    print(check, end=' ')
for i in range(n):
    checker(inp[i])