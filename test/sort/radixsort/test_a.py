from unittest import TestCase

from sort.radixsort.radixsort import get_radix_arr, inner_insert_sort, radix_sort


class TestA(TestCase):
    def test_get_radix_arr(self):
        arr = get_radix_arr([123, 234], 1)
        self.assertEqual(arr, [3, 4])

    def test_inner_insert_sort(self):
        arr = inner_insert_sort([133, 214], 2)
        self.assertEqual(arr, [214, 133])

    def test_radix_sort(self):
        arr = radix_sort([329, 457, 657, 839, 436, 720, 355], 3)
        self.assertEqual(arr, [329, 355, 436, 457, 657, 720, 839])
