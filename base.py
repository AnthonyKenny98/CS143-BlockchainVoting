import pickle
import time

class Block:
    """Provide a representation of a singular block in the blockchain.

    Attributes:
        time -- time time at which the block was created
        votes -- a frozenset of individuals' votes
        prev -- the previous block's hash
    """

    def __init__(self, votes, prev):
        self.time = time.time()
        self.votes = votes
        self.prev = prev

    def __hash__(self):
        """Override the built in hash function."""

        return hash(pickle.dumps(self))

    @property
    def prev(self):
        """Return the previous block's hash."""

        return self.prev

    @property
    def votes(self):
        """Return the votes recorded within the block."""

        return self.votes

    @property
    def time(self):
        """Return the time at which this block was created."""

        return self.time

class Vote(tuple):
    """Represent who voted for whom in a simple class object."""

    def __new__(self, voter, candidate):
        """Create a new tuple containing the name of both the voter and the
        candidate for whom she voted.
        """

        return tuple.__new__(self, (voter, candidate))

    @property
    def voter(self):
        """Return the voter's name."""
        return tuple.__getitem__(self, 0)

