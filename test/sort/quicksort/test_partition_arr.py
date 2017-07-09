from unittest import TestCase

from sort.quicksort.quicksort import partition_arr


class TestPartitionArr(TestCase):
    def test_partition_arr(self):
        arr = [2, 8, 7, 1, 3, 5, 6, 4]
        location = partition_arr(arr, 0, 7)
        self.assertEqual(location, 3)
