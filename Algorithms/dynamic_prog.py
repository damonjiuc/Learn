# Числа фибоначи

def fib_rec(n):
    """ O(fib(n)) через рекурсию """
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)

def fib_dyn(n):
    """ O(n) через ДП """
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]