from block import Block

import time

class InvalidBlockchain(Exception):
    """Alert the user that the blocks that he has specified to not make up a
    valid blockchain.
    """

    pass

class Blockchain(object):
    """Store a sort of linked list of Block objects in a set.

    Attributes:
        blocks -- set of blocks that make up the blockchain
    """

    def __init__(self, blocks=[]):
        self.creationTime = time.time()
        self.blocks = set()
        self.createGenesisBlock()

    def createGenesisBlock(self):
        genesisBlock = Block(None, None)
        if Block.isValidBlock(genesisBlock):
            self.blocks.add(genesisBlock)

    def add(self, block):
        """Add a block to the blockchain and return True if successful, False if
        unsuccessful.
        """

        #TODO more robust add function

        if self.verify(block) or (len(self.blocks) == 0 and block.prev == None):
            self.blocks.add(block)
            return True
        else:
            return False

    def block(self, hash_):
        """Find a block in the blockchain by its hash."""

        try:
            return list(filter(lambda b: hash(b) == hash_, self.blocks))[0]
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
            prevblock = list(filter(
                lambda b: hash(b) == prevhash,
                self.blocks
            ))[0]

            # Increment depth counter
            prevhash = prevblock.prev
            depth += 1

        return depth

    def verify(self, block):
        """Check that a particular block can be added to the chain by
        verifying all of the votes in the block.
        """

        if not Block.isValidBlock(block):
            return False

        prevhash = block.prev


        #SOMEHTING WRONG HERE
        while prevhash is not None:
            prevblock = self.block(prevhash)
            if not verifyBlockOnChain(block):
                return False
            prevhash = prevblock.prev

        return True


        # voter = block.vote.voter

        # while prevhash != None:
        #     # Identify the previous block in the blockchain
        #     prevblock = self.block(prevhash)
        #     prevvoter = prevblock.vote.voter

        #     # Check for bad votes
        #     if voter == prevvoter:
        #         return False

        #     prevhash = prevblock.prev

        # return True

    @property
    def last(self):
        """Get the block at the end of the longest chain."""

        try:
            return max(self.blocks, key=self.depth)
        except ValueError:
            return None

    @property
    def length(self):

        # Does not include the genesis block
        return self.depth(self.last)

    @staticmethod
    def isValidChain(chain):

        #TODO
        return True

def verifyBlockOnChain(block):
    return True