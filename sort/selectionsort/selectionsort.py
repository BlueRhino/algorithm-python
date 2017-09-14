def selection_sort(arr):
    length = len(arr)
    for i in range(0, length):
        min_index = i
        for j in range(length - 1, i, -1):
            if arr[j] < arr[min_index]:
                min_index = j
        tmp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = tmp
    return arr
