def radix_sort(arr, radix_length):
    for i in range(1, radix_length + 1):
        arr = inner_insert_sort(arr, i)
    return arr


def inner_insert_sort(arr, radix_index):
    """
    内部使用稳定的插入排序进行对每一位的排序
    :param arr:每个元素为十进制数的数组
    :param radix_index:
    :return:
    """
    # TODO:暂时没有考虑有的数位数不够的情况
    arr_len = len(arr)
    if arr_len < 2:
        return arr
    arr_radix = get_radix_arr(arr, radix_index)
    for i in range(1, arr_len):
        key_radix = arr_radix[i]
        key = arr[i]
        j = i - 1
        while j >= 0 and arr_radix[j] > key_radix:
            arr_radix[j + 1] = arr_radix[j]
            arr[j + 1] = arr[j]
            j -= 1
        arr_radix[j + 1] = key_radix
        arr[j + 1] = key
    return arr


def get_radix_arr(arr, radix_index):
    arr_radix = []
    mode_number = 10 ** radix_index
    divide_number = 10 ** (radix_index - 1)
    for arr_element in arr:
        arr_radix.append(int((arr_element % mode_number) / divide_number))
    return arr_radix
