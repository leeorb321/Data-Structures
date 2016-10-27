# -*- coding: utf-8 -*-

'''Implementation of Binary Search Tree.'''

from .tree import TreeNode, BinaryTree

class BST(BinaryTree):

    '''Binary Search Tree class.'''

    def __init__(self, root=None):
        super(BST, self).__init__(root)

    def search(self, val):
        '''Return True if val exists in tree else False.'''

        ptr = self.root
        while ptr is not None:
            if val == ptr.val:
                return ptr
            elif val < ptr.val:
                if ptr.left is not None:
                    ptr = ptr.left
                else:
                    return False
            elif val > ptr.val:
                if ptr.right is not None:
                    ptr = ptr.right
                else:
                    return False
        return False

    def insert(self, to_insert):
        '''Add node to tree.'''

        if not isinstance(to_insert, TreeNode):
            new_node = TreeNode(to_insert)
        else:
            new_node = to_insert

        if self.is_empty():
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, ptr, new_node):
        '''Private method for insertion, recursive.'''

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

    def remove(self, to_remove):
        '''Remove node from tree - by value or by reference.'''

        if not isinstance(to_remove, TreeNode):
            self._remove_by_val(to_remove)
        else:
            self._remove_by_ref(to_remove)

    def _remove_by_ref(self, node):
        '''Remove node from tree - by reference.'''

        # If node has no children
        if node.is_lone_leaf() is True:
            self.root = None
        if node.left is None and node.right is None:
            if node.is_left_child() is True:
                node.parent.left = None
            elif node.is_right_child() is True:
                node.parent.right = None
            else:
                node = None

        # If node has only one child
        elif node.left is None and node.right is not None:
            if node.is_left_child() is True:
                node.parent.left = node.right
            elif node.is_right_child() is True:
                node.parent.right = node.right
        elif node.left is not None and node.right is None:
            if node.is_left_child() is True:
                node.parent.left = node.left
            elif node.is_right_child() is True:
                node.parent.right = node.left

        # If node has both left and right children
        elif node.left and node.right:
            swap_node = self.get_swap_node(node)
            self.swap(node, swap_node)
            self._remove_by_ref(swap_node)
            # self._remove_by_ref(node)

    def _remove_by_val(self, val):
        '''Remove node from tree - by value.'''

        ptr = self.search(val)

        # If node has no children
        if ptr.is_lone_leaf() is True:
            self.root = None
        elif ptr.left is None and ptr.right is None:
            if ptr.is_left_child() is True:
                ptr.parent.left = None
            elif ptr.is_right_child() is True:
                ptr.parent.right = None
            else:
                ptr = None

        # If node has only one child
        elif ptr.left is None and ptr.right is not None:
            if ptr.is_left_child() is True:
                ptr.parent.left = ptr.right
            elif ptr.is_right_child() is True:
                ptr.parent.right = ptr.right
        elif ptr.left is not None and ptr.right is None:
            if ptr.is_left_child() is True:
                ptr.parent.left = ptr.left
            elif ptr.is_right_child() is True:
                ptr.parent.right = ptr.left

        # If node has both left and right children
        elif ptr.left and ptr.right:
            swap_node = self.get_swap_node(ptr)
            self.swap(ptr, swap_node)
            self._remove_by_ref(swap_node)
            # self._remove_by_ref(ptr)

    def swap(self, node1, node2):
        '''Swap two tree nodes.'''

        node1.val, node2.val = node2.val, node1.val

    def get_swap_node(self, node):
        '''Get node for swapping when removing node with two children.'''

        if node is None or node.is_lone_leaf():
            return None

        current = None

        # Get max val in left subtree
        if node.left is not None:
            current = node.left
            while current.right is not None:
                if current.right is not None:
                    current = current.right
                else:
                    return current

        elif node.right is not None:
            current = node.right
            while current.right is not None:
                if current.left is not None:
                    current = current.left
                else:
                    return current

        return current
