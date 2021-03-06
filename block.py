import pickle
import time
from hashlib import sha224

from election import Vote

class InvalidBlock(Exception):
    """Alert the user that the blocks that he has specified to not make up a
    valid blockchain.
    """
    pass

class Block(object):
    """Provide a representation of a singular block in the blockchain.

    Attributes:
        time -- time time at which the block was created
        votes -- a frozenset of individuals' votes
        prev -- the previous block's hash
    """

    def __init__(self, vote, prev):
        if isinstance(vote, Vote) or isinstance(vote, type(None)):
            self.time = time.time()
            self.vote = vote
            self.prev = prev
            self.nonce = 0
        else:
            raise InvalidBlock

    def __hash__(self):
        """Override the built in hash function."""

        return hash(pickle.dumps(self))

    def __repr__(self):
        return "BLOCK : [time : {}, vote : {}, prev : {}]".format(self.time, self.vote, self.prev)


    @staticmethod
    def isValidBlock(block):
        
        return True