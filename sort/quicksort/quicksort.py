def partition_arr(arr, start, end):
    """
    对输入数组arr在范围start及end之间的元素使用快速排序，使用arr[end]元素作为排序分界
    返回arr[end]元素的索引位置
    :param arr:
    :param start:
    :param end:
    :return:arr[end]元素的索引位置
    """
    if start < 0 or end < start:
        raise Exception("The index is not correct.")
    arr_len = len(arr)
    if end > arr_len - 1:
        raise Exception("The end index must less than the length of arr.")
    flag = arr[end]
    i = start - 1
    for j in range(start, end):
        if arr[j] <= flag:
            i += 1
            __exchange_value(arr, i, j)
    __exchange_value(arr, i + 1, end)
    return i + 1


def __exchange_value(arr, index1, index2):
    arr_len = len(arr)
    if 0 <= index1 < arr_len and 0 <= index2 < arr_len:
        if index1 == index2:
            return
        tmp = arr[index1]
        arr[index1] = arr[index2]
        arr[index2] = tmp
    else:
        raise Exception("Index is not correct.")
