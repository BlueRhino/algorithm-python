from unittest import TestCase

from sort.heapsort import heap_sort


class TestHeapSort(TestCase):
    def test_max_heapify(self):
        res = heap_sort.max_heapify([16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 1)
        self.assertEqual(res, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_build_max_heap(self):
        arr = heap_sort.build_max_heap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
        self.assertEqual(arr, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    def test_build_max_heap_one(self):
        arr = heap_sort.build_max_heap([4])
        self.assertEqual(arr, [4])

    def test_build_max_heap_zero(self):
        arr = heap_sort.build_max_heap([])
        self.assertEqual(arr, [])

    def test_check_is_max_heap(self):
        res = heap_sort.check_is_max_heap([4])
        self.assertEqual(res, True)
        res = heap_sort.check_is_max_heap([4, 1, 2])
        self.assertEqual(res, True)
        res = heap_sort.check_is_max_heap([4, 1, 2, 6])
        self.assertEqual(res, False)

    def test_check_subtree_is_max_heap(self):
        res = heap_sort.check_subtree_is_max_heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 1)
        self.assertEqual(res, False)
        res = heap_sort.check_subtree_is_max_heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 3)
        self.assertEqual(res, True)
        res = heap_sort.check_subtree_is_max_heap([16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 4)
        self.assertEqual(res, True)

    def test_max_heap_sort(self):
        arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        res = heap_sort.max_heap_sort(arr)
        self.assertEqual(res, [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])
