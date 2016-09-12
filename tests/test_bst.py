import unittest
import sys
from io import StringIO

from structures.bst import *


class TestBinaryTree(unittest.TestCase):

    def test_contructor(self):
        t = BST()
        self.assertTrue(t.is_empty())

        t2 = BST(TreeNode(4))
        self.assertEqual(t2.root.val, 4)

    def test_search(self):
        t = BST()
        t.root = TreeNode(2)
        t.root.add_left(TreeNode(1))
        t.root.add_right(TreeNode(3))

        ptr = t.search(3)
        self.assertEqual(ptr.val, 3)
        self.assertEqual(ptr, t.root.right)

        ptr = t.search(0)
        self.assertFalse(ptr)

        ptr = t.search(5)
        self.assertFalse(ptr)

    def test_add(self):
        t = BST()
        t.root = TreeNode(3)
        t.add(5)
        self.assertEqual(t.root.right.val, 5)
        self.assertFalse(t.root.left)

        t1 = BST()
        t1.add(2)
        t1.add(1)
        t1.add(3)
        self.assertEqual(t1.root.val, 2)
        self.assertEqual(t1.root.left.val, 1)
        self.assertEqual(t1.root.right.val, 3)

        t2 = BST()
        t1

    def test_remove_by_val_no_children(self):
        t = BST()
        t.add(2)
        self.assertFalse(t.is_empty())
        t.remove(2)
        self.assertTrue(t.is_empty())
        ptr = t.search(2)
        self.assertFalse(ptr)

        t1 = BST()
        t.add(2)
        t.add(3)
        t.add(1)

        ptr = t.search(3)
        self.assertTrue(ptr)
        t.remove(3)
        ptr = t.search(3)
        self.assertFalse(ptr)

        ptr = t.search(1)
        self.assertTrue(ptr)
        t.remove(1)
        ptr = t.search(1)
        self.assertFalse(ptr)

    def test_remove_by_ref_no_children(self):
        t = BST()
        t.add(2)
        self.assertFalse(t.is_empty())
        ptr = t.search(2)
        t.remove(ptr)
        self.assertTrue(t.is_empty())
        self.assertFalse(t.search(ptr.val))

        t1 = BST()
        t.add(2)
        t.add(3)
        t.add(1)

        ptr = t.search(3)
        self.assertTrue(ptr)
        t.remove(ptr)

        ptr = t.search(1)
        self.assertTrue(ptr)
        t.remove(ptr)
        self.assertFalse(t.search(ptr.val))

    def test_remove_by_val_one_child(self):
        t = BST()
        t.add(2)
        t.add(3)
        t.add(4)
        ptr = t.search(3)
        self.assertTrue(ptr)
        t.remove(3)
        ptr = t.search(3)
        self.assertFalse(ptr)
        ptr1 = t.search(4)
        self.assertEqual(t.root.right, ptr1)
        self.assertEqual(t.root.right.val, 4)

    def test_remove_by_ref_one_child(self):
        t = BST()
        t.add(2)
        t.add(3)
        t.add(4)
        three = t.search(3)
        self.assertTrue(three)
        t.remove(three)
        ptr = t.search(3)
        self.assertFalse(ptr)
        ptr1 = t.search(4)
        self.assertEqual(t.root.right, ptr1)
        self.assertEqual(t.root.right.val, 4)

    def test_swap(self):
        t = BST()
        t.add(2)
        t.add(1)
        t.add(4)
        self.assertEqual(t.root.right.val, 4)
        self.assertEqual(t.root.left.val, 1)

        t.swap(t.search(1), t.search(4))
        self.assertEqual(t.root.right.val, 1)
        self.assertEqual(t.root.left.val, 4)

    def test_get_swap_node(self):
        t = BST()
        t.add(2)
        t.add(1)
        t.add(4)
        ptr = t.get_swap_node(t.root)
        self.assertEqual(ptr.val, 1)

        t1 = BST()
        t1.add(2)
        t1.add(3)
        t1.add(4)
        ptr = t1.get_swap_node(t1.root)
        self.assertEqual(ptr.val, 3)


    def test_remove_by_val_two_children(self):
        t = BST()
        t.add(2)
        t.add(4)
        t.add(5)
        t.add(3)
        t.add(1)

        ptr = t.search(4)
        self.assertTrue(ptr)
        t.remove(4)
        ptr = t.search(4)
        self.assertFalse(ptr)
        ptr1 = t.search(3)
        self.assertEqual(t.root.right, ptr1)
        self.assertEqual(t.root.right.val, 3)

    def test_remove_by_ref_two_children(self):
        t = BST()
        t.add(2)
        t.add(4)
        t.add(5)
        t.add(3)
        t.add(1)

        t.remove(t.root)
        ptr = t.search(2)
        self.assertFalse(ptr)
        ptr1 = t.search(1)
        self.assertEqual(t.root, ptr1)
        self.assertEqual(t.root.val, 1)
        self.assertEqual(t.root.right.val, 4)
