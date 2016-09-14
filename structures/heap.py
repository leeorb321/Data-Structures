# -*- coding: utf-8 -*-

class Heap(object):

    '''Implementation of a (Minimum) Binary Heap object.'''

    def __init__(self, *args):
        self.items = [0] + [i for i in args]
        self.heap_size = len(args)
        if self.items != [0]:
            self.heapify()

    def insert(self, val):
        self.items.append(val)
        self.heap_size += 1
        if len(self.items) > 2:
            self.sift_up(self.heap_size)

    def sift_up(self, i):
        while i // 2 > 0:
            if self.items[i] < self.items[i//2]:
                self.swap(i, i//2)
            i //= 2

    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def extract_min(self):
        min_item = self.items[1]
        self.items[1] = self.items.pop()
        self.heap_size -= 1
        self.sift_down(1)
        return min_item

    def sift_down(self, i):
        while i*2 <= self.heap_size:
            min_child = self.get_min_child(i)
            if self.items[i] > self.items[min_child]:
                self.swap(i, min_child)
            i = min_child

    def get_min_child(self, i):
        if i*2 >= self.heap_size:
            return i*2
        else:
            return i*2 if self.items[i*2] < self.items[i*2 + 1] else i*2 + 1

    def heapify(self):
        i = self.heap_size // 2
        while i > 0:
            self.sift_down(i)
            i -= 1
