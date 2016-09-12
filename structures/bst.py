# -*- coding: utf-8 -*-

from .tree import TreeNode, BinaryTree

class BST(BinaryTree):

    '''Implementation of Binary Search Tree.'''

    def __init__(self, root=None):
        super(BST, self).__init__(root)

    def search(self, val):
        ptr = self.root
        while ptr != None:
            if val == ptr.val:
                return ptr
            elif val < ptr.val:
                if ptr.left != None:
                    ptr = ptr.left
                else:
                    return False
            elif val > ptr.val:
                if ptr.right != None:
                    ptr = ptr.right
                else:
                    return False
        return False

    def add(self, to_add):
        if not isinstance(to_add, TreeNode):
            new_node = TreeNode(to_add)
        else:
            new_node = to_add

        if self.is_empty():
            self.root = new_node
        else:
            self._add(self.root, new_node)

    def _add(self, ptr, new_node):
        if new_node.val < ptr.val:
            if ptr.left == None:
                ptr.add_left(new_node)
            else:
                self._add(ptr.left, new_node)
        else:
            if ptr.right == None:
                ptr.add_right(new_node)
            else:
                self._add(ptr.right, new_node)

    def remove(self, to_remove):
        if not isinstance(to_remove, TreeNode):
            self._remove_by_val(to_remove)
        else:
            self._remove_by_ref(to_remove)

    def _remove_by_ref(self, node):
        # If node has no children
        if node.is_lone_leaf() == True:
            self.root = None
        if node.left == None and node.right == None:
            if node.is_left_child() == True:
                node.parent.left = None
            elif node.is_right_child() == True:
                node.parent.right = None
            else:
                node = None

        # If node has only one child
        elif node.left == None and node.right != None:
            if node.is_left_child() == True:
                node.parent.left = node.right
            elif node.is_right_child() == True:
                node.parent.right = node.right
        elif node.left != None and node.right == None:
            if node.is_left_child() == True:
                node.parent.left = node.left
            elif node.is_right_child() == True:
                node.parent.right = node.left

        # If node has both left and right children
        elif node.left and node.right:
            swap_node = self.get_swap_node(node)
            self.swap(node, swap_node)
            self._remove_by_ref(swap_node)

    def _remove_by_val(self, val):
        ptr = self.search(val)

        # If node has no children
        if ptr.is_lone_leaf() == True:
            self.root = None
        elif ptr.left == None and ptr.right == None:
            if ptr.is_left_child() == True:
                ptr.parent.left = None
            elif ptr.is_right_child() == True:
                ptr.parent.right = None
            else:
                ptr = None

        # If node has only one child
        elif ptr.left == None and ptr.right != None:
            if ptr.is_left_child() == True:
                ptr.parent.left = ptr.right
            elif ptr.is_right_child() == True:
                ptr.parent.right = ptr.right
        elif ptr.left != None and ptr.right == None:
            if ptr.is_left_child() == True:
                ptr.parent.left = ptr.left
            elif ptr.is_right_child() == True:
                ptr.parent.right = ptr.left

        # If node has both left and right children
        elif ptr.left and ptr.right:
            swap_node = self.get_swap_node(ptr)
            self.swap(ptr, swap_node)
            self._remove_by_ref(swap_node)

    def swap(self, node1, node2):
        node1.val, node2.val = node2.val, node1.val

    def get_swap_node(self, node):
        if node == None or node.is_lone_leaf():
            return None

        current = None

        # Get max val in left subtree
        if node.left != None:
            current = node.left
            while current.right != None:
                if current.right != None:
                    current = current.right
                else:
                    return current

        elif node.right != None:
            current = node.right
            while current.right != None:
                if current.left != None:
                    current = current.left
                else:
                    return current

        return current
