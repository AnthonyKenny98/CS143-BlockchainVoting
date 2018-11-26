import unittest

from block import Block
from blockchain import Blockchain

from block import Block

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.genesis = Block(set([None]), None)
        self.chain = Blockchain(self.genesis)

    def test_check(self):
        block = Block(set(), hash(self.genesis))
        self.assertTrue(self.chain.check(block))
        block = Block(set([None]), hash(self.genesis))
        self.assertFalse(self.chain.check(block))
        block = Block(set(), 0)
        self.assertFalse(self.chain.check(block))

    def test_last(self):
        self.assertEqual(self.genesis, self.chain.last()[1])

if __name__ == '__main__':
    unittest.main()
