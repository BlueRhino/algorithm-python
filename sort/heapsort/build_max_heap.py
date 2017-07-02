def max_heapify(arr_a, index):
    """
    :param arr_a: 需要调整的数组，数组满足假设，以index为根的节点的左右子树满足大根堆定义
    :param index: 需要调整的节点
    :return: 
    """
    # TODO:没有判断异常情况
    left_root = index * 2 + 1
    right_root = index * 2 + 2
    arr_len = len(arr_a)
    largest = index
    if left_root < arr_len:
        if arr_a[left_root] > arr_a[index]:
            largest = left_root
    if right_root < arr_len:
        if arr_a[right_root] > arr_a[largest]:
            largest = right_root
    if largest != index:
        temp = arr_a[index]
        arr_a[index] = arr_a[largest]
        arr_a[largest] = temp
        arr_a = max_heapify(arr_a, largest)
    return arr_a
