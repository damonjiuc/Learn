#Квадратичные сортировки O(N**2)

def insert_sort(A):
    """Сортировка списка A вставками"""
    #Находим элемент, который не идет в порядке возрастания 
    # и перегоняем влево до тех пор, пока не начнет
    for top in range(1, len(A)):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]
            k -=1

def choise_sort(A):
    """Сортировка списка A выбором"""
    #Сравниваем по очереди элементы с первым, если текущий меньше,
    # то меняем их местами, далее двигаемся ко второрому элементу
    for top in range(len(A) - 1):
        for k in range(top + 1, len(A)):
            if A[k] < A[top]:
                A[top], A[k] = A[k], A[top]



def bubble_sort(A):
    """Сортировка списка A пузырьком"""
    #Идем слева направо, если текущий элемент больше следующего - 
    # меняем их местами, как только элемент всатет в конец - начинаем сеачала
    N = len(A)
    #top = N - 1
    #for k in range(N - 1):
    #    max = 0
    #    while max < top:
    #        if A[max] > A[max + 1]:
    #            A[max], A[max + 1] = A[max + 1], A[max]
    #            max +=1
    #        else:
    #            max +=1
    #    top -= 1
    for bypass in range(1, N):
        for max in range(N-bypass):
            if A[max] > A[max + 1]:
                A[max], A[max + 1] = A[max + 1], A[max]

def test_sort(sort_algorithm):
    print('Тестируем: ', sort_algorithm.__doc__) #Вывод Документ-строки
    print('testcase #1: ', end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')

    print('testcase #2: ', end='')
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(0, 20))
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')
    
    print('testcase #3: ', end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print('Ok' if A == A_sorted else 'Fail')
    
if __name__ == "__main__": #Вывод Документ-строки
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(bubble_sort)