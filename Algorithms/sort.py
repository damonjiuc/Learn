#Сортировки

def count_sort(A):
    """Сортировка подсчетом"""
    #Если элементы однотипные можно их пересчитать 
    count = [0]*10
    B = []
    for i in range(len(A)):
        count[A[i]] += 1
    for digit in range(10):
        while count[digit] > 0:
            B.append(digit)
            count[digit] -= 1
    for i in range(len(A)):
        A[i] = B[i]
    



def test_sort(sort_algorithm):
    print('Тестируем: ', sort_algorithm.__doc__) #Вывод Документ-строки
    print('testcase #1: ', end='')
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print(A)
    print('Ok' if A == A_sorted else 'Fail')

    print('testcase #2: ')
    A = list(range(0, 10)) + list(range(9, -1, -1)) + list(range(0, 10))
    print(A)
    sort_algorithm(A)
    print(A)
    
    print('testcase #3: ', end='')
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print(A)
    print('Ok' if A == A_sorted else 'Fail')
    
if __name__ == "__main__": #Вывод Документ-строки
    test_sort(count_sort)