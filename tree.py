# -*- coding: utf-8 -*-

class TreeNode(object):

    '''Implementation of Tree Node object.'''

    def __init__(self, val=None, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def add_left(self, node):
        if self.left == None:
            self.left = node
            self.left.parent = self
        else:
            return False

    def add_right(self, node):
        if self.right == None:
            self.right = node
            self.right.parent = self
        else:
            return False


class Tree(object):

    '''Implementation of Tree structure.'''

    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root == None

    def traverse(self, ptr):
        '''In-order traversal of the tree, starting at ptr.'''

        if ptr != None:
            print(ptr.val)
            self.traverse(ptr.left)
            self.traverse(ptr.right)


