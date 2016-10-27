# -*- coding: utf-8 -*-

from .linkedlist import ListNode, List

class Queue(List):

    '''Implementation of Queue data abstract.'''

    def __init__(self, *elements):
        super(Queue, self).__init__(*elements)

    def enqueue(self, val):
        '''Add val to end of queue.'''

        self.insert_tail(val)

    def dequeue(self):
        '''Remove and return item from head of queue.'''

        dequeued_element = self.head.val

        if self.is_empty():
            return False
        else:
            self.head = self.head.next_ptr
            if self.head is None:
                self.tail = self.head

        return dequeued_element

    def peek(self):
        '''Return item from head of queue without removing it.'''

        return self.head.val
