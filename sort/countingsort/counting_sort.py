def counting_sort(arr, min_value, max_value):
    if max_value < min_value:
        raise Exception('The max value is less than the min value.')
    arr_len = len(arr)
    res = [0 for x in range(0, arr_len)]
    gap = max_value - min_value + 1
    tmp = [0 for x in range(0, gap)]
    for i in range(0, arr_len):
        tmp[arr[i] - min_value] += 1
    for i in range(1, gap):
        tmp[i] += tmp[i - 1]
    for i in range(arr_len - 1, -1, -1):
        res[tmp[arr[i] - min_value] - 1] = arr[i]
        tmp[arr[i] - min_value] -= 1
    return res
