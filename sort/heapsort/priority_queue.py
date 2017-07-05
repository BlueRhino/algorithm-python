import math

from sort.heapsort.heap_sort import build_max_heap, max_heapify_with_len


class PriorityQueue:
    def __init__(self, arr):
        if len(arr) <= 1:
            raise Exception("can not build a priority queue with zero element.")
        self.max_heap = build_max_heap(arr)

    def get_max_heap(self):
        return self.max_heap

    def get_max(self):
        """
        返回优先队列最大元素
        :return:
        """
        self.__check_heap_not_empty()
        return self.max_heap[0]

    def extract_max(self):
        """
        取出优先队列最大元素，并将其在优先队列中删除
        :return:
        """
        self.__check_heap_not_empty()
        max_element = self.max_heap[0]
        heap_size = len(self.max_heap)
        self.max_heap[0] = self.max_heap[heap_size - 1]
        self.max_heap = max_heapify_with_len(self.max_heap, 0, heap_size - 1)[0:heap_size - 1]
        return max_element

    def increase_value(self, index, new_value):
        """
        将index的位置的元素置为新的值并保持最大堆定义，新值必须大于原值
        :param index:
        :param new_value:
        :return:
        """
        self.__check_heap_not_empty()
        if index < 0:
            raise Exception("The index must be an integer greater than zero.")
        if index > (len(self.max_heap) - 1):
            raise Exception("Index out of range.Index is:" + str(index)
                            + ".And size of arr is:" + str(len(self.max_heap)))
        old_value = self.max_heap[index]
        if old_value > new_value:
            raise Exception("The new value must greater than the old one.")
        self.max_heap[index] = new_value
        while index > 0:
            parent_index = math.floor((index - 1) / 2)
            if self.max_heap[index] > self.max_heap[parent_index]:
                tmp = self.max_heap[parent_index]
                self.max_heap[parent_index] = self.max_heap[index]
                self.max_heap[index] = tmp
                index = parent_index
            else:
                return

    def insert_value(self, value):
        """
        插入新节点到最大堆中，并且保持最大堆定义
        :param value:
        :return:
        """
        self.max_heap.append(value)
        self.increase_value(len(self.max_heap) - 1, value)

    def __check_heap_not_empty(self):
        if len(self.max_heap) <= 0:
            raise Exception("the priority queue is empty.")
