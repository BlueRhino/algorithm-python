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
    判断数组arr的index节点为根的子树是否为大根堆
    :param arr: 数组存储的二叉树
    :param index:子树的跟
    :return: 
    """
    arr_len = len(arr)
    return check_subtree_is_max_heap_with_len(arr, index, arr_len)


def check_subtree_is_max_heap_with_len(arr, index, arr_len):
    """
    判断数组arr的index节点为根的子树是否为大根堆，只处理前arr_len个节点
    :param arr_len:判断长度
    :param arr: 数组存储的二叉树
    :param index:子树的跟
    :return:
    """
    if index >= arr_len:
        return True
    left_root = index * 2 + 1
    right_root = index * 2 + 2
    if right_root >= arr_len:
        return True
    if left_root < arr_len and arr[left_root] > arr[index]:
        return False
    if right_root < arr_len and arr[right_root] > arr[index]:
        return False
    left_check = check_subtree_is_max_heap_with_len(arr, left_root, arr_len)
    right_check = check_subtree_is_max_heap_with_len(arr, right_root, arr_len)
    return left_check and right_check


def max_heapify(arr, index):
    """
    将arr数组index节点置为大根堆
    :param arr: 需要调整的数组，数组满足假设，以index为根的节点的左右子树满足大根堆定义
    :param index: 需要调整的节点
    :return: 
    """
    arr_len = len(arr)
    return max_heapify_with_len(arr, index, arr_len)


def max_heapify_with_len(arr, index, arr_len):
    """
    将arr数组index节点置为大根堆，只处理前arr_len个节点
    :param arr_len:
    :param arr: 需要调整的数组，数组满足假设，以index为根的节点的左右子树满足大根堆定义
    :param index: 需要调整的节点
    :return:
    """
    left_root = index * 2 + 1
    right_root = index * 2 + 2
    if not ((check_subtree_is_max_heap_with_len(arr, left_root, arr_len))
            and (check_subtree_is_max_heap_with_len(arr, right_root, arr_len))):
        raise Exception('The subtree is not a max heap')
    largest = index
    if left_root < arr_len:
        if arr[left_root] > arr[index]:
            largest = left_root
    if right_root < arr_len:
        if arr[right_root] > arr[largest]:
            largest = right_root
    if largest != index:
        temp = arr[index]
        arr[index] = arr[largest]
        arr[largest] = temp
        arr = max_heapify_with_len(arr, largest, arr_len)
    return arr


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


def max_heap_sort(arr):
    """
    根据输入的数组进行堆排序
    :param arr: 输入的无序数组
    :return: 输出按照元素大小由小到大的排序后数组
    """
    arr = build_max_heap(arr)
    arr_len = len(arr)
    for i in range(arr_len - 1, -1, -1):
        # 根为第一个元素，必为最大
        tmp = arr[0]
        arr[0] = arr[i]
        arr[i] = tmp
        max_heapify_with_len(arr, 0, i)
    return arr
