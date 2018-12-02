from blockchain import Blockchain
from block import Block
from election import Vote, Voter, Candidate

class BaseNode(object):

	def __init__(self, index, network):
		self.index = index
		self.name = "N{}".format(self.index)
		self.chain = Blockchain()
		self.network = network
		if len(network.nodes) > 0:
			self.announceNewNode()

	def announceNewNode(self):
		for peer in self.network.nodes:
			if peer is not self:
				peer.newNodeExists(self)

	def newNodeExists(self, newNode):
		newNode.consensus(self.chain)

	def castVote(self, vote):
		pass
		
	def announceNewBlock(self):
		for peer in self.network.nodes:
			if peer is not self:
				peer.consensus(self.chain)

	def consensus(self, chain):		
		newLength = chain.length
		currentLength = 0 if self.chain == None else self.chain.length
		if newLength > currentLength and Blockchain.isValidChain(chain):
			self.chain = chain
			return True
		return False

	def __repr__(self):
		return self.name

class Node(BaseNode):
	""" Node that acts with best intentions and upholds the blockchain """

	def __init__(self, index, network):
		BaseNode.__init__(self, index, network)
		

	def castVote(self, vote):
		block = Block(vote, hash(self.chain.last))
		proof = Blockchain.proofOfWork(block)
		if self.chain.addBlock(block, proof):
			self.announceNewBlock()
			return True
		return False		
		

class NaughtyNode(BaseNode):
	""" Node that acts with malicious intentions and attempts to break the blockchain """

	def __init__(self, index, network):
		BaseNode.__init__(self, index, network)

	def castVote(self, vote):
		block = Block(vote, hash(self.chain.last))
		proof = Blockchain.proofOfWork(block)
		if self.chain.addBlock(block, proof):
			self.announceNewBlock()
			return True
		return False	