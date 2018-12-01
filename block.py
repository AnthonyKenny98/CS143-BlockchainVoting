import pickle
import time

from election import Vote

class InvalidBlock(Exception):
    """Alert the user that the blocks that he has specified to not make up a
    valid blockchain.
    """

    pass

class Block:
    """Provide a representation of a singular block in the blockchain.

    Attributes:
        time -- time time at which the block was created
        votes -- a frozenset of individuals' votes
        prev -- the previous block's hash
    """

    def __init__(self, vote, prev):
        self.time = time.time()
        if not isinstance(vote, Vote):
            raise InvalidBlock
        self.vote = vote
        self.prev = prev

    def __hash__(self):
        """Override the built in hash function."""

        return hash(pickle.dumps(self))

    @property
    def prev(self):
        """Return the previous block's hash."""

        return self.prev

    @property
    def vote(self):
        """Return the votes recorded within the block."""

        return self.vote

    @property
    def time(self):
        """Return the time at which this block was created."""

        return self.time


def verifyBlock(block):
    # TODO

    return True
