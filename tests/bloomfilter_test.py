import unittest
import sys

from structures.bloom import *

class TestBloomFilter(unittest.TestCase):

    def test_contructor(self):
        bf = BloomFilter(555)
        self.assertEqual(bf._bv, 0)
        self.assertEqual(bf.size, 555)

    def test_add_check(self):
        bf = BloomFilter()
        bf.add(4)
        for i in range(20):
            if i == 4:
                self.assertTrue(bf.check(i))
            else:
                self.assertFalse(bf.check(i))

        bf.add('hello')
        self.assertTrue(bf.check('hello'))
        self.assertFalse(bf.check('goodbye'))

        bf.add('192.168.1.1')
        self.assertTrue(bf.check(('192.168.1.1')))
        self.assertFalse(bf.check(('192.168.1.2')))
