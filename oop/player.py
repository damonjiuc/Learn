from datetime import datetime as dt

class Player:

    __LVL, __HEALTH = 1, 100
    __slots__ = ['__lvl', '__health', '__born']

    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = dt.now()

    # Геттер
    @property
    def lvl(self):
        return self.__lvl, f'{dt.now() - self.__born}'

    # Сеттер
    @lvl.setter
    def lvl(self, change):
        self.__lvl += Player.__typeTest(change)
        if self.__lvl >= 100: self.__lvl = 100

    # Декоратор для изменения констант
    @classmethod
    def set_cls_field(cls, lvl=1, health=100):
        cls.__LVL = Player.__typeTest(lvl)
        cls.__HEALTH = Player.__typeTest(health)

    # Декоратор для проверки типа вводимых данных
    @staticmethod
    def __typeTest(value):
        if isinstance(value, int):
            return value
        else:
            raise TypeError ('Must be int')