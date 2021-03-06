# -*- coding: utf-8 -*-
from sys import stdout

class TreeNode(object):

    '''Implementation of Binary Tree Node object.'''

    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def insert_left(self, node):
        if self.left is None:
            self.left = node
            self.left.parent = self
        else:
            return False

    def insert_right(self, node):
        if self.right is None:
            self.right = node
            self.right.parent = self
        else:
            return False

    def is_left_child(self):
        if self.parent is None:
            return False
        if self.parent.left == self:
            return True
        return False

    def is_right_child(self):
        if self.parent is None:
            return False
        if self.parent.right == self:
            return True
        return False

    def is_lone_leaf(self):
        return not self.parent and not self.left and not self.right


class BinaryTree(object):

    '''Implementation of Binary Tree structure.'''

    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root is None

    def traverse(self, ptr, out=stdout):
        '''In-order traversal of the tree, starting at ptr.'''

        if ptr is not None:
            self.traverse(ptr.left)
            out.write(str(ptr.val)+'\n')
            self.traverse(ptr.right)
