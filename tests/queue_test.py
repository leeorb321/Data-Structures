import unittest
import sys
from io import StringIO

from structures.queue_structure import *

class TestLinkedList(unittest.TestCase):

    def test_contructor(self):
        q = Queue()
        self.assertEqual(q.head, None)
        self.assertEqual(q.tail, None)

        q = Queue(2,3,4)
        self.assertEqual(q.head.val, 2)
        self.assertTrue(type(q.head), ListNode)
        self.assertNotEqual(q.head, q.tail)

    def test_enqueue(self):
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(4)
        self.assertFalse(q.is_empty())
        q.enqueue(5)
        self.assertEqual(q.tail.val, 5)

    def test_dequeue(self):
        q = Queue(2,3,4)
        self.assertEqual(q.head.val, 2)
        front = q.dequeue()
        self.assertEqual(front, 2)
        self.assertEqual(q.head.val, 3)

    def test_peek(self):
        q = Queue(2,3,4)
        front = q.peek()
        self.assertEqual(front, 2)
        self.assertNotEqual(q.head.val, 3)
