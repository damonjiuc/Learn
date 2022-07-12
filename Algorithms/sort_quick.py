import random

# Сортировка слиянием

def merge(A:list, B:list):
    """ Слияние отсортированных массивов """
    C=[0] * (len(A) + len(B))
    i = k = n = 0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            n += 1
            i += 1
        else:
            C[n] = B[k]
            n += 1
            k += 1
    while i < len[A]:
        C[n] = A[i]
        n += 1
        i += 1
    while k < len(B):
        C[n] = B[k]
        n += 1
        k += 1
    return C

def merge_sort(A):
    """ Сортировка слиянием"""
    if len(A) <= 1:
        return
    middle = len(A) / 2
    L = [A[i] for i in range(0, middle)]
    R = [A[i] for i in range(0, middle)]
    merge_sort(L)
    merge_sort(R)
    C = merge(L, R)
    for i in range(len(A)):
        A[i] = C[i]

# Быстрая сортировка (Сортировка Тони Хоара)

def quick_sort(A):
    if len(A) <= 1:
        return
    L = []
    M = []
    R = []
    barrier = random.randrange(len(A))
    for x in A:
        for x in A:
            if x < barrier:
                L.append(x)
            elif x == barrier:
                M.append(x)
            else:
                R.append(x)
        quick_sort(L)
        quick_sort(R)
        k = 0                           #можно сделать через срезы
        for x in L + M + R:
            A[k] = x
            k += 1


