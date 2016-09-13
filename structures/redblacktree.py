# -*- coding: utf-8 -*-
from sys import stdout
from .tree import TreeNode, BinaryTree
from .bst import BST

class RedBlackNode(TreeNode):

    '''Implementation of Red-Black Balanced Binary Search Tree Node.'''

    def __init__(self, val=None, left=None, right=None, parent=None, color='red'):
        super(RedBlackNode, self).__init__(val, left, right, parent)
        self.color = color

    def _uncle(self):
        uncle = self.parent.parent.right if self.parent.is_left_child() else self.parent.parent.left
        return uncle


class RedBlackTree(BST):

    '''Implementation of Red-Black Balanced Binary Search Tree.
        1. Root is black
        2. No two reds in a row
        3. Always same number of blacks from root to None.
    '''

    def __init__(self, root=None):
        super(RedBlackTree, self).__init__(root)

    def insert(self, to_insert):
        if not isinstance(to_insert, TreeNode):
            new_node = RedBlackNode(to_insert)
        else:
            new_node = to_insert

        if self.is_empty():
            new_node.color = 'black'
            self.root = new_node
        else:
            self._insert(self.root, new_node)
            if new_node.parent.color == 'red':
                self.adjust(new_node)

    def _insert(self, ptr, new_node):
        if new_node.val < ptr.val:
            if ptr.left == None:
                ptr.insert_left(new_node)
            else:
                self._insert(ptr.left, new_node)
        else:
            if ptr.right == None:
                ptr.insert_right(new_node)
            else:
                self._insert(ptr.right, new_node)

    def adjust(self, new_node):
        if new_node._uncle().color == 'black':
            zigzag = False
            if new_node.is_left_child():
                if new_node.parent.is_right_child():
                    zigzag = True
                self.right_rotate(new_node)
                if zigzag:
                    self.left_rotate(new_node)
            else:
                if new_node.parent.is_left_child():
                    zigzag = True
                self.left_rotate(new_node)
                if zigzag:
                    self.right_rotate(new_node)
            if new_node.color == 'red' and new_node.parent.color == 'red':
                self.adjust(new_node)
        else:
            new_node.parent.parent.color = 'red'
            new_node.parent.color = 'black'
            new_node._uncle().color = 'black'
        if self.root.color == 'red':
            self.root.color == 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x.is_left_child():
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.parent
        y.left = x.right
        if x.right != None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == None:
            self.root = x
        elif y.is_right_child():
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def traverse(self, ptr, out=stdout):
        '''In-order traversal of the tree, starting at ptr.'''

        if ptr != None:
            self.traverse(ptr.left)
            out.write(str(ptr.val)+' '+str(ptr.color)+'\n')
            self.traverse(ptr.right)

