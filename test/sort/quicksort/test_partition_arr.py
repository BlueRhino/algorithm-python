from unittest import TestCase

from sort.quicksort.quicksort import partition_arr, quick_sort


class TestPartitionArr(TestCase):
    def test_partition_arr(self):
        arr = [2, 8, 7, 1, 3, 5, 6, 4]
        location = partition_arr(arr, 0, 7)
        self.assertEqual(location, 3)

    def test_quick_sort(self):
        arr = [2, 8, 7, 1, 3, 5, 6, 4]
        quick_sort(arr, 0, 7)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8])
