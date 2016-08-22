# -*- coding: utf-8 -*-

class ListNode(object):

    '''Implementation of Linked List Node object.'''

    def __init__(self, val=None, next=None):
        self.val = val
        if next == None or self.validate_next(next):
            self.next = next

    def validate_next(self, next):
        '''Validate that Node points to another valid node.'''
        if type(next) != ListNode:
            raise Exception('Next node must be of type \'ListNode\'')
        else:
            return True

class List(object):

    '''Implementation of Linked List data structure.'''

    def __init__(self, *values):
        '''Create instance of linked list, with values of initial nodes in the list.'''
        self.head = ListNode(values[0])
        current = self.head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        self.tail = current

    def traverse(self):
        '''Traverse Linked List and print out node values.'''
        current = self.head
        while current != None:
            print(current.val)
            current = current.next

    def insert_head(self, val):
        '''Insert new node at head of Linked List.'''
        self.head = ListNode(val, self.head)

    def insert_tail(self, val):
        '''Insert new node at end of Linked List.'''
        self.tail.next = ListNode(val)
        self.tail = self.tail.next

    def insert_after(self, node, val):
        '''Insert new node after a certain node in the Linked List.'''
        node.next = ListNode(val, node.next)

    def remove(self, val):
        '''Remove first occurrence of a node with a specified value.
        Return False if none found.'''
        current = self.head
        if current.val == val:
            self.head = self.head.next
            return True
        if current.next == None:
            return False
        while current.next.val != val:
            current = current.next
            if current.next == None:
                return False
        current.next = current.next.next
        return True

    def search(self, val):
        '''Return first occurrence of a node with a specified value or False if none found.'''
        current = self.head
        while current != None:
            if current.val == val:
                return current
            current = current.next
        return False





