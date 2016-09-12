# -*- coding: utf-8 -*-

from .tree import TreeNode, BinaryTree
from .bst import BST

class RedBlackNode(TreeNode):

    '''Implementation of Red-Black Balanced Binary Search Tree Node.'''

    def __init__(self, val=None, left=None, right=None, parent=None, color='black'):
        super(RedBlackNode, self).__init__(val, left, right, parent)
        self.color = color

class RedBlackTree(BST):

    '''Implementation of Red-Black Balanced Binary Search Tree.'''

    def __init__(self, root=None):
        super(RedBlackTree, self).__init__(root)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.root:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.root:
            self.root = y
        elif x.is_left_child():
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        x = y.left
        y.left = x.right
        if x.right != self.root:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.root:
            self.root = x
        elif y.is_right_child():
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x
