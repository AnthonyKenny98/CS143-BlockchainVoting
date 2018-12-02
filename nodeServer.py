from blockchain import Blockchain
from block import Block
from election import Vote, Voter, Candidate

class Node(object):

	def __init__(self, index, network):
		self.index = index
		self.name = "N{}".format(self.index)
		self.chain = Blockchain()
		self.network = network
		
		#### TODO: update nodes chain when node first joins network if there are other nodes in network
		if len(network.nodes) > 0:
			self.announceNewNode()

	def announceNewNode(self):
		for peer in self.network.nodes:
			if peer is not self:
				peer.newNodeExists(self)

	def newNodeExists(self, newNode):
		newNode.consensus(self.chain)

	def castVote(self, vote):
		block = Block(vote, hash(self.chain.last))
		proof = Blockchain.proofOfWork(block)
		if self.chain.addBlock(block, proof):
			self.announceNewBlock()
			return True
		return False
		
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