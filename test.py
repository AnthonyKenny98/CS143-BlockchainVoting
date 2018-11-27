import unittest

from blockchain import Blockchain
from hashable import Block, Vote

class TestBlock(unittest.TestCase):
    def setUp(self):
        self.b1 = Block(
            set([Vote('Owen', 'Marcus'), Vote('Anthony', 'Ronny')]),
            None
        )
        self.b2 = Block(
            set([Vote('Owen', 'Marcus'), Vote('Anthony', 'Ronny')]),
            self.b1.sha256()
        )
        self.b3 = Block(
            set([Vote('Owen', 'Marcus'), Vote('Anthony', 'Ronny')]),
            self.b2.sha256()
        )
        self.b4 = Block(
            set([Vote('Owen', 'Marcus'), Vote('Anthony', 'Ronny')]),
            self.b2.sha256()
        )
        self.b5 = Block(
            set([Vote('Owen', 'Marcus'), Vote('Amany', 'Ronny')]),
            self.b2.sha256()
        )

    def test_sha256(self):
        self.assertEqual(self.b1.sha256(), self.b1.sha256())
        self.assertNotEqual(self.b1.sha256(), self.b2.sha256())
        self.assertNotEqual(self.b2.sha256(), self.b3.sha256())
        self.assertNotEqual(self.b3.sha256(), self.b4.sha256())
        self.assertNotEqual(self.b3.sha256(), self.b5.sha256())

class TestVote(unittest.TestCase):
    def setUp(self):
        self.vote = Vote('Owen', 'Ronny')
        self.hash_ = self.vote.sha256()

    def test_sha256(self):
        self.assertEqual(self.hash_, self.vote.sha256())
        self.assertEqual(self.hash_, Vote('Owen', 'James').sha256())
        self.assertNotEqual(self.hash_, Vote('Amany', 'Ronny').sha256())
        self.assertNotEqual(self.hash_, Vote('Amany', 'Marcus').sha256())

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.genesis0 = Block(set(), None)
        self.genesis1 = Block(set([Vote('Amany', 'James')]), None)
        self.genesis2 = Block(
            set([Vote('Amany', 'James'), Vote('Owen', 'Ronny')]),
            None
        )
        self.chain0 = Blockchain(self.genesis0)
        self.chain1 = Blockchain(self.genesis1)
        self.chain2 = Blockchain(self.genesis2)

    def test_add(self):
        pass

    def test_check(self):
        self.assertTrue(
            self.chain0.check(Block(set(), self.genesis0.sha256())) != None
        )
        self.assertTrue(
            self.chain0.check(Block(set(), self.genesis1.sha256())) == None
        )
        self.assertTrue(self.chain0.check(Block(set(), None)) == None)
        self.assertTrue(
            self.chain0.check(Block(
                set([Vote('Owen', 'James'), Vote('Anthony', 'James')]),
                self.genesis0.sha256()
            )) != None
        )
        self.assertTrue(
            self.chain0.check(Block(
                set([Vote('Owen', 'James'), Vote('Owen', 'Marcus')]),
                self.genesis0.sha256()
            )) == None
        )

    def test_last(self):
        pass

if __name__ == '__main__':
    unittest.main()
