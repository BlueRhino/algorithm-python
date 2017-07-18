from unittest import TestCase

from sort.countingsort.counting_sort import counting_sort


class TestCountingSort(TestCase):
    def test_counting_sort(self):
        arr = [2, 5, 3, 0, 2, 3, 0, 3]
        arr = counting_sort(arr, 0, 5)
        self.assertEqual(arr, [0, 0, 2, 2, 3, 3, 3, 5])

    def test_counting_sort_negative(self):
        arr = [2, 7, 3, 0, 2, 3, -4, 3]
        arr = counting_sort(arr, -4, 7)
        self.assertEqual(arr, [-1, 0, 2, 2, 3, 3, 3, 5])
