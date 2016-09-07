# -*- coding: utf-8 -*-

from tree import TreeNode, BinaryTree

class BST(BinaryTree):

    '''Implementation of Binary Search Tree.'''

    def __init__(self, root=None):
        super(BST, self).__init__(root)

    def search(self, val, ptr=self.root):
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
            self._remove_by_val(to_remove.val)

    def _remove_by_val(self, val):
        ptr = self.search(val)
        if ptr.is_left_child() == True:
            ptr.parent.left = ptr.left
            if ptr.right > ptr.left:
                ptr.parent.left.right = ptr.right
            else:
                ptr.parent.left.left = ptr.right
        elif ptr.is_right_child() == True:
            ptr.parent.right = ptr.right
            if ptr.left < ptr.right:
                ptr.parent.right.left = ptr.left
            else:
                ptr.parent.right.right = ptr.right
