import unittest
import sys

from structures.redblacktree import *


class TestRedBlackTree(unittest.TestCase):

    def test_constructor(self):
        t = RedBlackTree()
        self.assertTrue(t.is_empty())
        t2 = RedBlackTree(TreeNode(4))
        self.assertEqual(t2.root.val, 4)

    # def test_left_rotate(self):
    #     t = RedBlackTree()
    #     t.insert(3)
    #     t.insert(5)
    #     t.insert(4)
    #     t.insert(2)
    #     t.insert(8)
    #     t.insert(6)
    #     t.insert(9)
    #     x = t.search(5)
    #     y = t.search(8)

    #     self.assertEqual(x.left.val, 4)
    #     self.assertEqual(x.right, y)
    #     self.assertEqual(y.left.val, 6)

    #     t.left_rotate(x)

    #     self.assertEqual(x.right.val, 6)
    #     self.assertEqual(y.left, x)
    #     self.assertEqual(y.left.val, 5)

    # def test_right_rotate(self):
    #     t = RedBlackTree()
    #     t.insert(8)
    #     t.insert(3)
    #     t.insert(5)
    #     t.insert(4)
    #     t.insert(2)
    #     t.insert(6)
    #     t.insert(9)
    #     x = t.search(3)
    #     y = t.search(8)

    #     self.assertEqual(x.left.val, 2)
    #     self.assertEqual(y.left, x)
    #     self.assertEqual(y.left.val, 3)

    #     t.right_rotate(x)

    #     self.assertEqual(x.right.val, 8)
    #     self.assertEqual(x.right, y)
    #     self.assertEqual(y.left.val, 5)
