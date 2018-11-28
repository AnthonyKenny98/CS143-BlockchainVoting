from base import Block, Vote

class InvalidBlockchain(Exception):
    """Alert the user that the blocks that he has specified to not make up a
    valid blockchain.
    """

    pass

class Blockchain:
    """Store a sort of linked list of Block objects in a set.

    Attributes:
        blocks -- set of blocks that make up the blockchain
    """

    def __init__(self, blocks=[]):
        # Remove duplicates
        initpool = set(blocks)
        lastapproved = frozenset(blocks)

        # Store the hashes of the last batch of approved blocks
        self.blocks = set()

        while len(initpool) > 0:
            if len(self.blocks) == 0:
                # Find the genesis block
                geneses = filter(lambda b: b.prev == None, initpool)

                if len(geneses) != 1 or self.add(geneses[0]) == False:
                    # There must be exactly one genesis block
                    raise InvalidBlockchain

                lastapproved = frozenset(map(hash, geneses))
                initpool.discard(geneses[0])
            else:
                candidates = frozenset(
                    filter(lambda b: b.prev in lastapproved, initpool)
                )

                if len(candidates) < 1:
                    # None of the other blocks fit into the chain
                    raise InvalidBlockchain

                # Attempt to add the newly-approved blocks to the blockchain
                status = map(self.add, candidates)

                if False in status:
                    # Votes in every block must be verified
                    raise InvalidBlockchain

                lastapproved = frozenset(map(hash, candidates))
                initpool -= candidates

    def add(self, block):
        """Add a block to the blockchain and return True if successful, False if
        unsuccessful.
        """

        if self.verify(block) or (len(self.blocks) == 0 and block.prev == None):
            self.blocks.add(block)
            return True
        else:
            return False

    def block(self, hash_):
        """Find a block in the blockchain by its hash."""

        try:
            return filter(lambda b: hash(b) == hash_, self.blocks)[0]
        except IndexError:
            return None

    def depth(self, block):
        """Calculate the depth of the specified block if it exists in the
        chain.
        """

        # The genesis block has depth 0
        prevhash = block.prev
        depth = 0

        while prevhash != None:
            # Find the previous block in the blockchain
            prevblock = filter(
                lambda b: hash(b) == prevhash,
                self.blocks
            )[0]

            # Increment depth counter
            prevhash = prevblock.prev
            depth += 1

        return depth

    def last(self):
        """Get the block at the end of the longest chain."""

        try:
            return max(self.blocks, key=self.depth)
        except ValueError:
            return None

    def verify(self, block):
        """Check that a particular block can be added to the chain by
        verifying all of the votes in the block.
        """

        prevhash = block.prev
        voters = frozenset(map(lambda v: v.voter, block.votes))

        # Check for bad votes (e.g. double votes)
        if prevhash == None or len(voters) != len(block.votes):
            return False

        while prevhash != None:
            # Identify the previous block in the blockchain
            prevblock = self.block(prevhash)
            prevvoters = frozenset(map(lambda v: v.voter, prevblock.votes))

            # Check for bad votes
            if prevvoters - voters != prevvoters:
                return False

            prevhash = prevblock.prev

        return True

