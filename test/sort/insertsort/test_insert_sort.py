from unittest import TestCase

from sort.insertsort.insertsort import insert_sort


class TestInsertSort(TestCase):
    def test_insert_sort(self):
        arr = [5, 2, 6, 4, 1, 3]
        arr = insert_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6])
