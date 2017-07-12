def insert_sort(arr):
    arr_len = len(arr)
    if arr_len < 2:
        return arr
    for i in range(1, arr_len):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
