mas = 'gup zup lip but gif dot beh bet bac nos mex nap jif vif jep leh liq got gys giq zec gyx let vop gox dif mas zux bix zik zys bat vop lex zik lyf nic bap vaq jaq ryh mac mop lef vit vyx zup bih lox zik vyx raq leq jop lup rap dyh vyc bex dic lec vis jaq loc dec ret muf gex gep joq mak vyk zah guk bep gax nex mek dys goh zux zuf liq vuf vyh bec doq jyh rec mef doh mus vix bik get baf zyc zoc nut gec lyx vax duc mik rof lyk laq jyt zah jes dec vof bis gep gaf nat zit vyp dit vix nuq ryk nah box gop ruf jet bok bec mek buh nok vac zof bat nit vyc nep jak gys vys ruc lop ric rep rit rox mut bec bas jis ruk zak joc nox doq vit dyf bes lat laf juc luk veh zak dek nas gap rap des mep rah lyh jok vat luf zat zup zuc rap def nec gex zut dak byh rik ziq mos bus muh max zyp lyk rif rit dit jut jit zep nup jot duq dap rox zax byq mup jis bix nyf moc leh maf vuh dyq lec dup riq vut mys vyq jic ros mih ziq ric def vux vaf bif nox nyt nuc jup myt lex lap vyh ryk rih neh bip nuh jec luc rak ruc myp rof gup zef mic nuq vyt bup met gaq mex rup baf vof res rok vuf ric ruf bet lyt juc nut vip lep zus mep goh rix bas nyt lyx mat noh luc myt jef nyp dyq net rit dak juc nuh bek mux gah vas mah jof zot vaq mih vyx end'
splited = mas.split(' ')
proper = []
words = list(set(splited))
count = []
for i in range(len(words)):
    count.append(0)
for i in range(len(splited)):
    if splited[i] in words:
        count[words.index(splited[i])] += 1
for i in range(len(words)):
    if count[i] > 1:
        proper.append(words[i])
proper.sort()
print(' '.join(proper))