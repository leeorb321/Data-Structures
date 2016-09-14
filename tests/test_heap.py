import unittest
import sys
from io import StringIO

from structures.heap import *

class TestHeap(unittest.TestCase):

    def test_contructor(self):
        h1 = Heap()
        self.assertEqual(h1.items, [0])
        h2 = Heap(4,5,3,2)
        self.assertEqual(h2.heap_size, 4)

    def test_insert(self):
        h1 = Heap()
        h1.insert(3)
        self.assertEqual(h1.items, [0,3])
        self.assertEqual(h1.heap_size, 1)

        h2 = Heap(4)
        h2.insert(2)
        self.assertEqual(h2.items, [0,2,4])
        self.assertEqual(h2.heap_size, 2)

    def sift_up(self):
        h1 = Heap()
        h1.items = [0,4,5,3,2]
        h1.sift_up(4)
        self.assertEqual(h1.items, [0,2,4,3,5])
        h1.sift_up(1)
        self.assertEqual(h1.items, [0,2,4,3,5])

        h2 = Heap()
        h2.items = [0,4,5,3,2]
        h2.sift_up(3)
        self.assertEqual(h1.items, [0,3,5,4,2])

    def test_swap(self):
        h = Heap()
        h.items = [0,4,5,3,2]
        h.swap(1,2)
        self.assertEqual(h.items, [0,5,4,3,2])

    def test_extract_min(self):
        h = Heap(4,5,3,2)
        m = h.extract_min()
        self.assertEqual(m, 2)
        self.assertEqual(h.heap_size, 3)
        self.assertEqual(h.items, [0,3,4,5])

    def test_sift_down(self):
        h = Heap()
        h.items = [0,9,4,5,3,2]
        h.heap_size = len(h.items) - 1
        h.sift_down(1)
        self.assertEqual(h.items, [0,4,2,5,3,9])

    def test_get_min_child(self):
        h = Heap(9,4,5,3,2)
        m = h.get_min_child(1)
        self.assertEqual(h.items[m], 3)

    def test_heapify(self):
        h = Heap(9,4,5,3,2)
        self.assertEqual(h.items, [0,2,3,5,9,4])
