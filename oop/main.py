class Purse:

    def __init__(self, currency, name='Unknown'):
        if currency not in ('USD', 'RUR'):
            raise ValueError
        self.__money = 0.0
        self.currency = currency
        self.name = name

    def up_the_balance(self, howmuch):
        self.__money = self.__money + howmuch
        return howmuch

    def low_the_balance(self, howmuch):
        if self.__money - howmuch < 0:
            print('Не достаточно средств')
            raise ValueError ('Не достаточно средств')
        self.__money = self.__money - howmuch
        return howmuch

    def info(self):
        print(self.__money)

    def __del__(self):
        print('Кошелек удален')



x = Purse('USD')
y = Purse('USD', 'Damon')
y.up_the_balance(16)
x.up_the_balance(y.low_the_balance(6))
x.info()
y.info()