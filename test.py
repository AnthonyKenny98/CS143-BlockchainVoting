import unittest

from block import Block
from election import Vote
from blockchain import Blockchain, InvalidBlockchain

ab = {
    'jy': Vote('Amany', 'James'),
    'mc': Vote('Amany', 'Marcus'),
    'rk': Vote('Amany', 'Ronny')
}

ak = {
    'jy': Vote('Anthony', 'James'),
    'mc': Vote('Anthony', 'Marcus'),
    'rk': Vote('Anthony', 'Ronny')
}

on = {
    'jy': Vote('Owen', 'James'),
    'mc': Vote('Owen', 'Marcus'),
    'rk': Vote('Owen', 'Ronny')
}



class TestBlock(unittest.TestCase):
    """Test the functionality of our semi-custom hash function."""

    def setUp(self):
        """Set up five blocks to test against one another."""

        self.b1 = Block([on['mc'], ak['rk']], None)
        self.b2 = Block([on['mc'], ak['rk']], hash(self.b1))
        self.b3 = Block([on['mc'], ak['rk']], hash(self.b2))
        self.b4 = Block([on['mc'], ak['rk']], hash(self.b2))
        self.b5 = Block([on['mc'], ab['rk']], hash(self.b2))

    def test_hash(self):
        """Ensure that the only time that two blocks have the same hash is when
        the two blocks are the same block (i.e. all attributes are the same).
        """

        self.assertEqual(hash(self.b1), hash(self.b1))
        self.assertNotEqual(hash(self.b1), hash(self.b2))
        self.assertNotEqual(hash(self.b2), hash(self.b3))
        self.assertNotEqual(hash(self.b3), hash(self.b4))
        self.assertNotEqual(hash(self.b3), hash(self.b5))

class TestBlockchain(unittest.TestCase):
    """Make sure that the Blockchain class behaves correctly."""

    def setUp(self):
        """Set up some blocks that can be combined in different ways to form
        valid and invalid blockchains.
        """

        self.b1 = Block([on['jy']], None)
        self.b2 = Block([on['mc']], hash(self.b1))
        self.b3 = Block([ab['jy']], hash(self.b1))
        self.b4 = Block([ab['mc']], hash(self.b1))
        self.b5 = Block([ab['rk'], ab['mc']], hash(self.b1))
        self.b6 = Block([ak['rk']], hash(self.b3))
        self.b7 = Block([ak['rk'], on['rk']], hash(self.b3))

    def test_init(self):
        """Ensure that the constructor only allows users to create valid
        blockchains.

        This test also tests the add, block, and verify functions.
        """

        self.assertTrue(isinstance(Blockchain(), Blockchain))
        self.assertTrue(isinstance(Blockchain([self.b1]), Blockchain))
        self.assertTrue(isinstance(Blockchain([self.b1, self.b1]), Blockchain))
        self.assertTrue(
            isinstance(Blockchain([self.b1, self.b3, self.b3]), Blockchain)
        )
        self.assertTrue(
            isinstance(Blockchain([self.b1, self.b3, self.b6]), Blockchain)
        )
        self.assertTrue(isinstance(
            Blockchain([self.b1, self.b3, self.b4, self.b6]), Blockchain
        ))
        with self.assertRaises(InvalidBlockchain):
            Blockchain([self.b2])
        with self.assertRaises(InvalidBlockchain):
            Blockchain([self.b1, self.b6])
        with self.assertRaises(InvalidBlockchain):
            Blockchain([self.b1, self.b2])
        with self.assertRaises(InvalidBlockchain):
            Blockchain([self.b1, self.b5])
        with self.assertRaises(InvalidBlockchain):
            Blockchain([self.b1, self.b3, self.b4, self.b7])

    def test_depth(self):
        chain = Blockchain([self.b1, self.b3, self.b4, self.b6])
        self.assertEqual(chain.depth(self.b1), 0)
        self.assertEqual(chain.depth(self.b3), 1)
        self.assertEqual(chain.depth(self.b4), 1)
        self.assertEqual(chain.depth(self.b6), 2)

    def test_last(self):
        c1 = Blockchain()
        c2 = Blockchain([self.b1])
        c3 = Blockchain([self.b1, self.b1])
        c4 = Blockchain([self.b1, self.b3, self.b3])
        c5 = Blockchain([self.b1, self.b3, self.b6])
        c6 = Blockchain([self.b1, self.b3, self.b4, self.b6])
        self.assertEqual(c1.last(), None)
        self.assertEqual(c2.last(), self.b1)
        self.assertEqual(c3.last(), self.b1)
        self.assertEqual(c4.last(), self.b3)
        self.assertEqual(c5.last(), self.b6)
        self.assertEqual(c6.last(), self.b6)

if __name__ == '__main__':
    unittest.main()
