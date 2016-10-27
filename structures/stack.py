# -*- coding: utf-8 -*-

class Stack(object):

    '''Implementation of the stack data structure.'''

    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            self.items = items[:]

    def push(self, item):
        '''Push item onto top of the stack.'''

        self.items.append(item)

    def pop(self):
        '''Pop item from top of the stack.'''

        return self.items.pop()

    def peek(self):
        '''Return item from top of the stack without removing it.'''

        return self.items[-1]

    def is_empty(self):
        '''Return True if stack is empty, False otherwise.'''

        return len(self.items) == 0
