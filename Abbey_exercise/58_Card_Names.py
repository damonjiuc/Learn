n = 30
mas = '41 48 6 26 7 35 50 31 16 40 33 1 5 47 19 49 37 17 36 46 24 28 51 43 15 8 30 13 4 9'
splited = mas.split(' ')
inted = []
for i in range(n):
    inted.append(int(splited[i]))
suits = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
for i in range(n):
    card_value = inted[i]
    suit_value = card_value // 13
    rank_value = card_value % 13
    suit = suits[suit_value]
    rank = ranks[rank_value]
    print(f'{rank}-of-{suit}', end=' ')

