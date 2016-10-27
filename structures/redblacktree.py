# -*- coding: utf-8 -*-
from sys import stdout
from .tree import TreeNode
from .bst import BST

class RedBlackNode(TreeNode):

    '''Implementation of Red-Black Balanced Binary Search Tree Node.'''

    def __init__(self, val=None, left=None, right=None, parent=None, color='red'):
        super(RedBlackNode, self).__init__(val, left, right, parent)
        self.color = color

    def _uncle(self):
        uncle = self.parent.parent.right if self.parent.is_left_child() else self.parent.parent.left
        return uncle

    def _sibling(self):
        if not self.parent:
            return False
        if self.is_left_child():
            return self.parent.right if self.parent.right else False
        else:
            return self.parent.left if self.parent.left else False


class RedBlackTree(BST):

    '''Implementation of Red-Black Balanced Binary Search Tree.
        1. Root is black
        2. No two reds in a row
        3. Always same number of blacks from root to None.
    '''

    def __init__(self, root=None):
        super(RedBlackTree, self).__init__(root)

    def insert(self, to_insert):
        '''Add new node to tree.'''

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
            if ptr.left is None:
                ptr.insert_left(new_node)
            else:
                self._insert(ptr.left, new_node)
        else:
            if ptr.right is None:
                ptr.insert_right(new_node)
            else:
                self._insert(ptr.right, new_node)

    def adjust(self, new_node):
        '''Adjust new_node's subtree to reflect correct structure.'''

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
            self.root.color = 'black'

    def left_rotate(self, x):
        '''Perform left rotation, starting at node 'x'.'''

        y = x.right
        x.right = y.left
        if y.left is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x.is_left_child():
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        '''Perform right rotation, starting at node 'x'.'''

        y = x.parent
        y.left = x.right
        if x.right is not None:
            x.right.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y.is_right_child():
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def traverse(self, ptr, out=stdout):
        '''In-order traversal of the tree, starting at ptr.'''

        if ptr is not None:
            self.traverse(ptr.left)
            out.write(str(ptr.val)+' '+str(ptr.color)+'\n')
            self.traverse(ptr.right)

    def xor_red(self, node1, node2):
        '''Check if only one of node1, node2 is red.'''

        if not node2:
            return node1 if node1.color == 'red' else False
        if not (node1.color == 'red') ^ (node2.color == 'red'):
            return False
        else:
            return node1 if node1.color == 'red' else node2


    def remove(self, to_remove):
        '''Remove node from tree.'''

        to_remove = to_remove if isinstance(to_remove, RedBlackNode) else self.search(to_remove)

        if to_remove.left or to_remove.right:
            child = to_remove.left if to_remove.left else to_remove.right
            red = self.xor_red(to_remove, child)
        if red:
            red.color = 'black'
            super(RedBlackNode, self)._remove_by_ref(to_remove)
        else:
            to_remove.color = 'double black'
            self._remove_double_black(to_remove)
            super(RedBlackNode, self)._remove_by_ref(to_remove)


    def red_children(self, node):
        '''Return which children of node are red.'''

        if node.right and node.right.color == 'red':
            return node.right if (not node.left or node.left.color != 'red') else 'both'
        elif node.left and node.left.color == 'red':
            return node.left

    def _remove_double_black(self, node):
        sibling = node.sibling()
        if sibling.color == 'black':
            reds = self.red_children(sibling)
            if reds:
                if reds == 'both' or reds == sibling.left:
                    self.right_rotate(node)                # both cases and left-left case
                    if sibling.is_right_child():           # left-right case
                        self.right_rotate(node.parent.left)

                elif reds == 'both' or reds == sibling.right:
                    self.left_rotate(node.parent) # both cases and right-right case
                    if sibling.is_left_child():   # right-left case
                        self.left_rotate(node.parent.right)
            else:
                self.adjust(node)
        else:
            pass
