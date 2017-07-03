from unittest import TestCase

from sort.heapsort import heap_sort


class TestBuildMaxHeap(TestCase):
    def test_max_heapify(self):
        res = heap_sort.max_heapify([16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 1)
        self.assertEquals(res, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_build_max_heap(self):
        arr = heap_sort.build_max_heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        self.assertEquals(arr, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_build_max_heap_one(self):
        arr = heap_sort.build_max_heap([4])
        self.assertEquals(arr, [4])

    def test_build_max_heap_zero(self):
        arr = heap_sort.build_max_heap([])
        self.assertEquals(arr, [])

    def test_check_is_max_heap(self):
        res = heap_sort.check_is_max_heap([4])
        self.assertEquals(res, True)
        res = heap_sort.check_is_max_heap([4, 1, 2])
        self.assertEquals(res, True)
        res = heap_sort.check_is_max_heap([4, 1, 2, 6])
        self.assertEquals(res, False)

    def test_check_subtree_is_max_heap(self):
        res = heap_sort.check_subtree_is_max_heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 1)
        self.assertEquals(res, False)
        res = heap_sort.check_subtree_is_max_heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 3)
        self.assertEquals(res, True)
        res = heap_sort.check_subtree_is_max_heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 4)
        self.assertEquals(res, True)
