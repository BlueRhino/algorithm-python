from unittest import TestCase

from sort.mergesort.merge_sort import merge_inner, merge_sort


class TestMergeSort(TestCase):
    def test_merge_inner(self):
        arr = [2, 3, 4, 2, 4, 5, 7, 1, 2, 3, 6, 7, 8, 9, 0]
        arr = merge_inner(arr, 3, 7, 10)
        self.assertEqual(arr, [2, 3, 4, 1, 2, 2, 3, 4, 5, 6, 7, 7, 8, 9, 0])

    def test_merge_sort(self):
        arr = [5, 2, 4, 7, 1, 3, 2, 6]
        arr = merge_sort(arr, 0, 7)
        self.assertEqual(arr, [1, 2, 2, 3, 4, 5, 6, 7])
