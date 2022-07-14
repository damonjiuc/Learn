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

# Наибольшая общая подпоследовательность (длина)
# A и B - массивы
# F(ij) длина наибольшей возможной подпоследовательности частей A и B
# A[0:i] - часть A содержащая первые i элементов, B[0:j] - -//-

def lcs(A, B):
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = 1 + F[i - 1][j - 1]
            else:
                F[i][j] = max(F[i - 1][j], F[i][j - 1])
    return F[-1][-1]

# Наибольшая возрастающая подпоследовательность (длина)
# F(i) - НВП для части A[0:i], которая заканчивается и содержит элемент a(i) = A[i - 1]
# F(j) = max(F[j] + 1); j < i; a(i) > a(j)
# F(0) = 0

def lis(A):
    F = [0] * (len(A) + 1)
    for i in range(1, len(A) + 1):
        max = 0
        for j in range(0, i):
            if A[i - 1] > A[j - 1] and F[j] > max:
                max = F[j]
        F[i] = max + 1
    return F[len(A)]

#print(lis([1, 6, 5, 6, 7, 4, 2]))

# Редакцонное расстояние между строками (Левенштейна)
# F(ij) - минимальное расстояние между строками A[:i] и B[:j]
# F(ij) = F(i-1)(j-1) if A(i) == B(j) // 1 + min(F(i-1)(j), F(i)(j-1), F(i-1)(j-1))

def levenstein(A, B):
    F = [[i + j if i * j == 0 else 0 for j in range(len(B) + 1)] for i in range(len(A) + 1)] # Крайние случаи
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1]
            else:
                F[i][j] = 1 + min(F[i -1][j], F[i][j - 1], F[i - 1][j - 1])
    return F[len(A)][len(B)]

print(levenstein('кит', 'коты'))

# Проверка равенства строк O(N)

def equal(A, B):
    if len(A) != len(B):
        return False
    for i in range(len(A)):
        if A[i] != B[i]:
            return False
    return True

# Поиск подстроки в строке O(N*M)

def search_substring(s, sub):
    for i in range(0, len(s) - len(sub)):
        if equal(s[i:i + len(sub)], sub):
            print(i)
