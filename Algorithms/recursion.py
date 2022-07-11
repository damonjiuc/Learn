# Рекурсия
# У каждого вызова функции свой набор имен, существующий до завершения функции / return(а)

def matryoshka(n):
    #n-глубина рекурсии
    if n == 0:
        print('Микроматрёшка')
    else:
        print('Верх матрёшки #', n)
        matryoshka(n-1)
        print('Низ матрёшки #', n)

#matryoshka(5)

def factorial(n:int):
    assert n >= 0, 'Факториал отрицательного не определен' #выведет ошибку при отрицательном n
    if n == 0:
        return 1
    return factorial(n - 1) * n

#print(factorial(4))

def gcd(a, b):
    """Алгоритм Эвклида
       Наименьший общий делитель a и b
    """
    if a == b:
        return a
    elif a > b:
        return gcd(a - b, b)
    elif a < b:
        return gcd(a, b - a)

#print(gcd(21, 7))

def gcd_mod(a, b):
    """Модифицированный вариант алгоритма Эвклида
       Через остаток от делоения
    """
    if b == 0:
        return a
    else:
        return gcd_mod(b, a % b)

#print(gcd_mod(21, 7))

def exp(x, n):
    """Быстрое возведение в степень"""
    if n == 0:
        return 1
    elif n % 2 == 1:
        return(exp(x, n-1) * x)
    else: #n % 2 == 0
        return exp(x**2, n//2)

#print(exp(2, 16))