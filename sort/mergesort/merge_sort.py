import math


def merge_inner(arr, p, q, r):
    """
    归并部分有序的数组，数组arr中元素下标p到q及q+1到r两部分已完成排序
    :param arr:
    :param p:
    :param q:
    :param r:
    :return:
    """
    if p <= q < r:
        arr_part1 = arr[p:q + 1]
        arr_part2 = arr[q + 1:r + 1]
        if len(arr_part1) == 0:
            i = 0
            for k in range(p, r + 1):
                arr[k] = arr_part2[i]
                i += 1
            return arr
        else:
            flag = max(arr_part1[-1], arr_part2[-1]) + 1
        arr_part1.append(flag)
        arr_part2.append(flag)
        i, j = 0, 0
        for k in range(p, r + 1):
            if arr_part1[i] <= arr_part2[j]:
                arr[k] = arr_part1[i]
                i += 1
            else:
                arr[k] = arr_part2[j]
                j += 1
        return arr
    else:
        raise Exception("error input parameters.p={0},q={1},r={2}".format(p, q, r))


def merge_sort(arr, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(arr, p, q)
        merge_sort(arr, q + 1, r)
        merge_inner(arr, p, q, r)
    return arr
