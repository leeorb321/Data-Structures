'''Implementation of Bloom Filter.'''

class BloomFilter(object):

    '''Bloom Filter Class.'''

    def __init__(self, size=1000):
        self._bv = 0
        self.size = size

    def add(self, item):
        '''Add item to filter.'''

        hash_idx = self._hash(item) - 1
        self._bv |= (1 << hash_idx)

    def _hash(self, item):
        hashed = 5381
        for char in str(item):
            hashed = (((hashed << 5) + hashed) + ord(char)) % self.size
        return hashed

    def check(self, item):
        '''Return True if item has been added to filter, else False.'''

        hash_idx = self._hash(item) - 1
        return (self._bv & (1 << hash_idx)) != 0
