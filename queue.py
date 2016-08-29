from linkedlist import ListNode, List

class Queue(List):

    '''Implementation of Queue data abstract.'''

    def __init__(self, *elements):
        super(Queue, self).__init__(*elements)

    def enqueue(self, val):
        self.insert_tail(val)

    def dequeue(self):
        dequeued_element = self.head.val

        if self.is_empty():
            return False
        else:
            self.head = self.head.next_ptr
            if self.head == None:
                self.tail = self.head

        return dequeued_element



