n = 6
k = 8
mas = ['NWCZ AKWZM IVL AMDMV GMIZA IOW QV IVKQMVB XMZAQI BPMZM EIA I SQVO.', 'TWDMAB BPWC UM XMBMZ IZM EWVLMZA UIVG BWTL I LIG IB BPM ZIKMA.', 'OZMMVNQMTLA IZM OWVM VWE BPIB ITT UMV IZM KZMIBML MYCIT.', 'BPM WVKM IVL NCBCZM SQVO KITTML QB BPM ZQAQVO ACV.', 'UMB I EWUIV IB BPM EMTT KIZBPIOM UCAB JM LMABZWGML.', 'I VQOPB IB BPM WXMZI.']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
c_letters = []
for i in range(k, 26):
    c_letters.append(letters[i])
for i in range(k):
    c_letters.append(letters[i])
letters.append(' ')
letters.append('.')
c_letters.append(' ')
c_letters.append('.')
print(c_letters)
for i in range(n):
    c_string = []
    string = mas[i]
    for u in range(len(string)):
        for y in range(28):
            if string[u] == letters[y]:
                c_string.append(letters[c_letters.index(letters[y])])
    print(''.join(c_string), end=' ')


