def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - 1, i, -1):
            if arr[j] < arr[j - 1]:
                tmp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = tmp
    return arr
