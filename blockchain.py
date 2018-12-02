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
        creation time -- time chain was initialized
        blocks -- set of blocks that make up the blockchain
    """

    code = '1'
    difficulty = 2

    def __init__(self):
        self.creationTime = time.time()
        self.blocks = []
        self.createGenesisBlock()

    def __repr__(self):
        lastBlock = self.last
        chain = [lastBlock.vote]
        prevHash = lastBlock.prev
        while prevHash is not None:
            prevBlock = self.block(prevHash)
            chain = [prevBlock.vote] + chain
            prevHash = prevBlock.prev
        return str(chain)

    def createGenesisBlock(self):
        """ Creates a genesis block with a None Vote."""
        genesisBlock = Block(None, None)
        if Block.isValidBlock(genesisBlock):
            self.blocks.append(genesisBlock)

    def addBlock(self, block, proof=""):
        """Add a block to the blockchain and return True if successful, False if
        unsuccessful.

        Should go through the following logic:

            * The previous_hash referred in the block and the hash of latest block
            in the chain match.
            * The submitted proof is valid
            * Extra checks specific to election implementation
        """

        prevHash = hash(self.last)

        if prevHash != block.prev:
            return False

        if not Blockchain.isValidProof(block, proof):
            return False

        # TODO: Add more election checks of validity

        self.blocks.append(block)
        return True


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
    def proofOfWork(block):
        blockHash = str(hash(block))
        while not blockHash.startswith(Blockchain.code * Blockchain.difficulty):
            block.nonce += 1
            blockHash = str(hash(block))
        return blockHash

    @staticmethod
    def isValidProof(block, proof):
        return (str(proof).startswith(Blockchain.code * Blockchain.difficulty)) and \
            (str(proof) == str(hash(block)))

    @staticmethod
    def isValidChain(chain):

        result = True
        previousHash = None

        for block in chain.blocks:
            block_hash = hash(block)

            if (previousHash != block.prev) or \
                not Blockchain.isValidProof(block, hash(block)) and block.prev != None:
                result = False
                break
            previousHash = hash(block)
        return result