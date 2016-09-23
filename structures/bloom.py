class BloomFilter(object):

    def __init__(self, size=1000):
        self.bv = 0
        self.size = size

    def add(self, item):
        hash_idx = self._hash(item) - 1
        self.bv |= (1 << hash_idx)

    def _hash(self, item):
        hashed = 5381
        for c in str(item):
            hashed = (((hashed << 5) + hashed) + ord(c)) % self.size
        return hashed

    def check(self, item):
        hash_idx = self._hash(item) - 1
        return (self.bv & (1 << hash_idx)) != 0
