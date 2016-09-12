import unittest
import sys
from io import StringIO

from structures.tree import *

class TestTreeNode(unittest.TestCase):

    def test_contructor(self):
        node1 = TreeNode()
        self.assertEqual(node1.val, None)
        self.assertEqual(node1.left, None)
        self.assertEqual(node1.right, None)
        self.assertEqual(node1.parent, None)

        node2 = TreeNode(3, left=node1)
        node1.parent = node2
        self.assertEqual(node1.parent, node2)
        self.assertEqual(node2.left, node1)
        self.assertEqual(node2.val, 3)

    def test_insert_left(self):
        node1 = TreeNode(4)
        node2 = TreeNode(3)
        node1.insert_left(node2)
        self.assertEqual(node1.left, node2)
        self.assertEqual(node2.parent, node1)

    def test_insert_right(self):
        node1 = TreeNode(4)
        node2 = TreeNode(3)
        node1.insert_right(node2)
        self.assertEqual(node1.right, node2)
        self.assertEqual(node2.parent, node1)

    def test_is_left_child(self):
        node1 = TreeNode(4)
        node2 = TreeNode(3)
        node1.insert_left(node2)
        self.assertTrue(node2.is_left_child())

    def test_is_right_child(self):
        node1 = TreeNode(4)
        node2 = TreeNode(3)
        node1.insert_right(node2)
        self.assertTrue(node2.is_right_child())

    def test_is_lone_leaf(self):
        node1 = TreeNode(4)
        self.assertTrue(node1.is_lone_leaf())
        node2 = TreeNode(3)
        node1.insert_right(node2)
        self.assertFalse(node1.is_lone_leaf())
        self.assertFalse(node2.is_lone_leaf())


class TestBinaryTree(unittest.TestCase):

    def test_contructor(self):
        node1 = TreeNode(4)
        t = BinaryTree(node1)
        self.assertEqual(t.root, node1)
        self.assertEqual(t.root.left, None)

        t1 = BinaryTree(TreeNode(3))
        self.assertEqual(t1.root.val, 3)

    def test_is_empty(self):
        t = BinaryTree()
        self.assertTrue(t.is_empty())
        t.root = TreeNode(3)
        self.assertFalse(t.is_empty())

    def test_traverse(self):
        t = BinaryTree(TreeNode(2))
        t.root.insert_left(TreeNode(4))
        t.root.insert_right(TreeNode(5))
        out = StringIO()
        t.traverse(t.root, out=out)
        output = out.getvalue().strip()
        self.assertEqual(output, '2')

        # TODO fix recursive testing
