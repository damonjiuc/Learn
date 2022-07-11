def binary_search(list, number):
    """Бинарный поиск
       Принимает массив и число, которое нужно найти
       Возвращает найденое число
    """
    low = 0
    high = len(list) - 1
    trynum = 1


    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == number:
            print(f'!!!Успех!!! Попытка номер {trynum}, число: {guess}')
            return mid
        if guess > number:
            print(f'Попытка номер {trynum}, число {guess} больше {number}')
            high = mid -1
        elif guess < number:
            print(f'Попытка номер {trynum}, число {guess} меньше {number}')
            low = mid + 1
        trynum += 1
    print(f'Поиск не дал результатов')
    return none

def massive_from_progression(number):
    """Создание массива - арифмитеческой прогрессии"""
    list = []
    i = 0

    while i != number:
        i += 1
        list.append(int(i))
    return(list)

list = massive_from_progression(654321)
binary_search(list, 123456)