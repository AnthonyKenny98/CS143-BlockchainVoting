# Blockchain Voting Platform


##block.py

### Block
A block is a simple object containing the time of its creation, a `Vote` 
object, and the hash of the previous block in the blockchain.


## blockchain.py

### BlockChain

The blockchain class is much more complex. A blockchain is implemented as a set
of `Block` objects. There are a number of methods associated with the
`Blockchain` class.

1. The `add` method adds a block  to the  blockchain. Before the block can be
added to the chain, it must first be verified by the `verify` function.

2. The `block` method looks up a block in the blockchain by its hash. If it
cannot find a block with the specified hash, it returns `None`.

3. The `depth` method gives the depth of the specified block in the blockchain.
The genesis block is at depth 0.

4. The `last` method returns the block at the end of the longest branch of the
blockchain. In other words, it returns block with the maximum depth.

5. The `verify` method ensures that a particular block fits into the
blockchain. To do this, it makes sure that the hash of the previous block is
the hash of a block that exists in the blockchain. It also makes sure that none
of the votes in the current block were made by voters who have already voted.

## election.py

### Election
Object that simulates the election

### Candidate
Object representing candidate that can be voted for

### Voter
Object representing a voter

### Vote

A vote is pretty much just a glorified tuple. The first item in the tuple is
the name of the person who is voting. The second item in the tuple is the name
of the candidate for whom the voter is voting.


## network.py

Contains everything required to set up the blockchain network.
Network object is a simplified view of all nodes, and each Node represents a 
voting machine