from unittest import TestCase

from sort.heapsort.heap_sort import check_is_max_heap
from sort.heapsort.priority_queue import PriorityQueue


class TestPriorityQueue(TestCase):
    def test_get_max(self):
        arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        priority_queue = PriorityQueue(arr)
        self.assertEqual(priority_queue.get_max(), 16)

    def test_extract_max(self):
        arr = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
        priority_queue = PriorityQueue(arr)
        self.assertEqual(priority_queue.extract_max(), 16)
        self.assertEqual(check_is_max_heap(priority_queue.get_max_heap()), True)
