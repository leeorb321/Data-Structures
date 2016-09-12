import unittest
import sys
from io import StringIO

from structures.linkedlist import *

class TestListNode(unittest.TestCase):

    def test_contructor(self):
        node = ListNode()
        self.assertEqual(node.val, None)
        self.assertEqual(node.next_ptr, None)

    def test_constructor_with_next(self):
        temp = ListNode()
        node1 = ListNode(val=3, next_ptr=temp)
        self.assertEqual(node1.next_ptr, temp)

        node2 = ListNode(val=3, next_ptr=2)
        self.assertEqual(node2.next_ptr.val, 2)

    def test_add_next(self):
        node1 = ListNode(val=2)
        node1.add_next(4)
        self.assertEqual(node1.next_ptr.val, 4)
        self.assertTrue(isinstance(node1.next_ptr, ListNode))

    def test_link_nodes(self):
        node1 = ListNode(val=2)
        node2 = ListNode(val=3)
        node1.link_nodes(node2)
        self.assertEqual(node1.next_ptr, node2)

    def test_validate_pointer(self):
        temp = ListNode()

        node = 2
        self.assertFalse(temp.validate_pointer(node))
        node = ListNode()
        self.assertTrue(temp.validate_pointer(node))
        node = ListNode(3)
        self.assertTrue(temp.validate_pointer(node))
        node = ListNode(val=4, next_ptr=ListNode(5))
        self.assertTrue(temp.validate_pointer(node))



class TestLinkedList(unittest.TestCase):

    def test_contructor(self):
        l1 = List()
        self.assertEqual(l1.head, None)
        self.assertEqual(l1.tail, None)

        l2 = List(1,2,3)
        self.assertEqual(l2.head.val, 1)
        self.assertNotEqual(l2.head, l2.tail)
        self.assertEqual(type(l2.head), ListNode)

        self.assertNotEqual(l2.head.next_ptr, None)
        self.assertEqual(l2.tail.next_ptr, None)

    def test_traverse(self):
        l = List(2,3,4,5)
        out = StringIO()
        l.traverse(out=out)
        output = out.getvalue().strip()
        self.assertEqual(out.getvalue(), '2\n3\n4\n5\n')

    def test_insert_head(self):
        l = List(2,3,4,5)
        self.assertEqual(l.head.val, 2)
        l.insert_head(55)
        self.assertEqual(l.head.val, 55)

    def test_insert_tail(self):
        l = List(2,3,4,5)
        self.assertEqual(l.tail.val, 5)
        l.insert_tail(55)
        self.assertEqual(l.tail.val, 55)

    def test_insert_after(self):
        l = List(2,3,4,5)
        ptr = l.search(3)
        self.assertEqual(ptr.next_ptr.val, 4)
        l.insert_after(ptr, 22)
        self.assertEqual(ptr.next_ptr.val, 22)

    def test_remove(self):
        l = List(2,3,4,5)
        ptr = l.search(3)
        self.assertTrue(ptr)
        l.remove(3)
        ptr = l.search(3)
        self.assertFalse(ptr)

    def test_search(self):
        l = List(2,3,4,5)
        ptr = l.search(3)
        self.assertTrue(ptr)
        ptr = l.search(22)
        self.assertFalse(ptr)

    def test_is_empty(self):
        l = List()
        self.assertTrue(l.is_empty())
        l.insert_tail(3)
        self.assertFalse(l.is_empty())



