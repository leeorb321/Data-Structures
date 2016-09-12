import unittest

from structures.stack import *

class TestStack(unittest.TestCase):

    def test_contructor(self):
        s1 = Stack()
        self.assertEqual(s1.items, [])

        s2 = Stack([1,2,3])
        self.assertEqual(len(s2.items), 3)
        self.assertEqual(s2.items, [1,2,3])

    def test_push(self):
        s1 = Stack()
        s1.push(3)
        s1.push(2)
        self.assertEqual(len(s1.items), 2)
        self.assertEqual(s1.items, [3,2])

    def test_pop(self):
        s1 = Stack()
        s1.push(3)
        s1.push(2)
        popped = s1.pop()
        self.assertEqual(len(s1.items), 1)
        self.assertEqual(s1.items, [3])
        self.assertEqual(popped, 2)

    def test_peek(self):
        s1 = Stack()
        s1.push(3)
        s1.push(2)
        peeked1 = s1.peek()
        popped = s1.pop()
        peeked2 = s1.peek()
        self.assertEqual(peeked1, 2)
        self.assertEqual(peeked2, 3)
        self.assertEqual(len(s1.items), 1)

    def test_is_empty(self):
        s1 = Stack()
        s1.push(3)
        self.assertFalse(s1.is_empty())
        s1.pop()
        self.assertTrue(s1.is_empty())
