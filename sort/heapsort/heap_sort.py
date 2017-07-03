import math


def check_is_max_heap(arr):
    """
    判断某数组是不是大根堆
    :param arr: 数组存储的二叉树
    :return: 
    """
    arr_len = len(arr)
    if arr_len < 2:
        return True
    last_parent_index = int(math.floor(arr_len / 2)) - 1
    for i in range(0, last_parent_index + 1):
        left_index = last_parent_index * 2 + 1
        right_index = last_parent_index * 2 + 2
        if left_index < arr_len:
            if arr[left_index] > arr[i]:
                return False
        if right_index < arr_len:
            if arr[right_index] > arr[i]:
                return False
    return True


def check_subtree_is_max_heap(arr, index):
    """
    判断某子树是不是最大堆
    :param arr: 数组存储的二叉树
    :param index:子树的跟
    :return: 
    """
    arr_len = len(arr)
    if index >= arr_len:
        return False
    left_root = index * 2 + 1
    right_root = index * 2 + 2
    if right_root >= arr_len:
        return True
    if left_root < arr_len & arr[left_root] > arr[index]:
        return False
    if right_root < arr_len & arr[right_root] > arr[index]:
        return False
    return check_subtree_is_max_heap(arr, left_root) & check_subtree_is_max_heap(arr, right_root)


def max_heapify(arr_a, index):
    """
    :param arr_a: 需要调整的数组，数组满足假设，以index为根的节点的左右子树满足大根堆定义
    :param index: 需要调整的节点
    :return: 
    """
    left_root = index * 2 + 1
    right_root = index * 2 + 2
    if check_subtree_is_max_heap(left_root) & check_subtree_is_max_heap(right_root):
        raise Exception('The subtree is not a max heap')
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


def build_max_heap(arr):
    """
    根据输入的数组创建大根堆，使用逆向遍历非叶子节点的方式
    :param arr: 输入数组
    :return: 使用数组存储的大根堆
    """
    arr_len = len(arr)
    if arr_len < 2:
        return arr
    last_parent_index = int(math.floor(arr_len / 2)) - 1
    for i in range(last_parent_index, -1, -1):
        arr = max_heapify(arr, i)
    return arr
