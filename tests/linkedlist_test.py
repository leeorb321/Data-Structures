import unittest

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
        pass
