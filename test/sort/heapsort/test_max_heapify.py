from unittest import TestCase

from sort.heapsort import build_max_heap


class TestMaxHeapify(TestCase):
    def test_max_heapify(self):
        res = build_max_heap.max_heapify([16, 4, 10, 14, 7, 9, 3, 2, 8, 1], 1)
        self.assertEquals(res, [16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
