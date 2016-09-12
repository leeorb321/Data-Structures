import unittest
import sys

from structures.redblacktree import *


class TestRedBlackTree(unittest.TestCase):

    def test_constructor(self):
        t = RedBlackTree()
        self.assertTrue(t.is_empty())
        t2 = RedBlackTree(TreeNode(4))
        self.assertEqual(t2.root.val, 4)

    def test_left_rotate(self):
        t = RedBlackTree()
        t.insert(3)
        t.insert(5)
        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(7)
        t.insert(8)
        x = t.search(5)

        t.left_rotate(x)
