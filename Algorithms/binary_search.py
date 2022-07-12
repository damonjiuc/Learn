#Бинарный поиск

def left_bound(A, key):
    """ Принимает массив и элемент, который нужно найти 
        возвращает индекс элемента слева от искомого
    """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] < key:
            left = middle
        else:
            right = middle
    return left

def right_bound(A, key):
    """ Принимает массив и элемент, который нужно найти 
        возвращает индекс элемента справа от искомого
    """
    left = -1
    right = len(A)
    while right - left > 1:
        middle = (left + right) // 2
        if A[middle] <= key:
            left = middle
        else:
            right = middle
    return right

def bin_search(A, key):
    left = left_bound(A, key)
    right = right_bound(A, key)
    count = right - left - 1
    if count == 0:
        print(f'Такого ключа нету в массиве, он мог бы находится между элементами {left} и {right}!')
    elif count == 1:
        print(f'Ключ {key} находятся в массиве на месте {left + 1}!')
    else:
        print(f'{count} ключей {key} находятся в массиве между элементами {left} и {right}!')


A = [1, 3, 5, 5, 5, 7, 9]         
bin_search(A, 1)
bin_search(A, 5)
bin_search(A, -1)
bin_search(A, 10)
bin_search(A, 4)

