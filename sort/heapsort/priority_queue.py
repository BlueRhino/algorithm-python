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

    def __check_heap_not_empty(self):
        if len(self.max_heap) <= 0:
            raise Exception("the priority queue is empty.")
