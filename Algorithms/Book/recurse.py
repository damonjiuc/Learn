def sum(arr):
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + sum(arr[1:])
#print(sum([1, 2, 3, 4]))

def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])

#print(count([1, 2, 3]))

def max(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

#print(max([1, 8, 6, 4]))

def quicksort(array):
    """Быстрая сотировка, через рекурсию"""
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        print(f'Опорная: {pivot}')
        less = [i for i in array[1:] if i <= pivot]
        print(f'Меньше: {less}')
        greater = [i for i in array[1:] if i > pivot]
        print(F'Больше: {greater}')
        print(less + [array[0]] + greater)
        return quicksort(less) + [pivot] + quicksort(greater)
print(quicksort([10, 5, 2, 3]))