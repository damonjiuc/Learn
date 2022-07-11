def findsmallest(arr):
    smallest = arr[0]
    samallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            samallest_index = i
    return samallest_index

def selectionsort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findsmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionsort([1, 9, 7, 3, 6, 4, 2, 8]))