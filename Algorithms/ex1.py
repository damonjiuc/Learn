# Сумма чисел от 0 до n
#Дано целое число n≥0. Вычислите сумму чисел 0+1+...+n
#sum0n(n) получающет в качестве параметра значение n и возвращающей нужную сумму.
def sum0n(n):
    if n == 0:
        return 0
    else:
        return sum0n(n-1) + n
#print(sum0n(5))

#Сумма цифр числа
#Дано целое число n>0. Посчитайте сумму его цифр 
#Функции sum_of_digits(n), возвращает сумму цифр числа n.
def sum_of_digits(n):
    if n // 10 == 0:
        return n
    else:
        return sum_of_digits(n // 10) + n % 10
#print(sum_of_digits(179))

#Минимальная цифра числа 
#Дано целое число n>0. Функция min_digit(n), возвращает значение минимальной цифры числа n
def min_digit(n):
    if n // 10 == 0:
        return n
    else:
        return min(min_digit(n // 10), n % 10)
#print(min_digit(179))

#Является ли число степенью двойки
#Дано целое число n>0. Функции is_power2(n), возвращающет значение типа bool. 
#Для чисел 1, 2, 4, 8 и т.д. функция должна возвращать True, для остальных чисел — False.
def is_power2(n):
    if n <= 2:
        return n % 2 == 0
    else:
        return is_power2(n / 2)
#print(is_power2(9))

#Напишите рекурсивную функцию fib(n), которая по данному целому неотрицательному n возвращает n-e число Фибоначчи.
def fib(n):
    if n in (1, 2):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)