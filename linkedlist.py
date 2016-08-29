# -*- coding: utf-8 -*-

class ListNode(object):

    '''Implementation of Linked List Node object.'''

    def __init__(self, val=None, next_ptr=None):
        self.val = val
        if next_ptr == None or self.validate_pointer(next_ptr):
            self.next_ptr = next_ptr
        elif next_ptr != None:
            self.add_next(next_ptr)

    def add_next(self, val):
        '''Add next_ptr to current node.'''
        self.next_ptr = ListNode(val)

    def link_nodes(self, next_node):
        if self.validate_pointer(next_node):
            self.next_ptr = next_node

    def validate_pointer(self, pointer):
        '''Validate that Node points to another valid node.'''
        if type(pointer) != type(self):
            raise Exception('Node must point only to other valid Nodes.')
        else:
            return True

class List(object):

    '''Implementation of Linked List data structure.'''

    def __init__(self, *values):
        '''Create instance of linked list, with values of initial nodes in the list.'''
        if not values:
            self.head = None
            self.tail = None
        else:
            self.head = ListNode(values[0])
            current = self.head
            for val in values[1:]:
                current.next_ptr = ListNode(val)
                current = current.next_ptr
            self.tail = current

    def traverse(self):
        '''Traverse Linked List and print out node values.'''
        current = self.head
        while current != None:
            print(current.val)
            current = current.next_ptr

    def insert_head(self, val):
        '''Insert new node at head of Linked List.'''
        if self.head != None:
            self.head = ListNode(val, self.head)
        else:
            self.head = ListNode(val, self.head)
            self.tail = self.head

    def insert_tail(self, val):
        '''Insert new node at end of Linked List.'''
        if self.tail == None:
            self.insert_head(val)
        else:
            self.tail.next_ptr = ListNode(val)
            self.tail = self.tail.next_ptr

    def insert_after(self, node, val):
        '''Insert new node after a certain node in the Linked List.'''
        node.next_ptr = ListNode(val, node.next_ptr)
        if node.next_ptr.next_ptr == None:
            self.tail = node.next_ptr

    def remove(self, val):
        '''Remove first occurrence of a node with a specified value.
        Return False if none found.'''
        if self.is_empty():
            return False

        current = self.head

        # Check if val is in the head node and remove if found.
        if current.val == val:
            self.head = self.head.next_ptr
            if self.head.next_ptr == None:
                self.tail = self.head
            return True
        if current.next_ptr == None:
            return False

        while current.next_ptr.val != val:
            current = current.next_ptr
            if current.next_ptr == None:
                return False

        current.next_ptr = current.next_ptr.next_ptr
        if current.next_ptr == None:
            self.tail = current

        return True

    def search(self, val):
        '''Return first occurrence of a node with a specified value or False if none found.'''
        current = self.head
        while current != None:
            if current.val == val:
                return current
            current = current.next_ptr
        return False

    def is_empty(self):
        return self.head == self.tail == None


