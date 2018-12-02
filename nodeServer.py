from blockchain import Blockchain
from block import Block
from election import Vote, Voter, Candidate

class Node(object):

	def __init__(self, index, network):
		self.index = index
		self.name = "N{}".format(self.index)
		self.chain = None
		self.network = network
		
		# TODO: update nodes chain when node first joins network if there are other nodes in network
		if len(network.nodes) > 0:
			self.consensus


	#TODO: somewhere in castVote/addBlock, i think proof of work calculation goes
	def castVote(self, vote):
		if self.chain == None:
			block = Block(vote, None)
		else:
			block = Block(vote, hash(self.chain.last()))
		self.addBlock(block)


	def addBlock(self, block):
		if self.chain == None:
			chain = Blockchain([block])
			if Blockchain.isValidChain(chain):
				self.chain = chain
				self.announceNewBlock()
		else:
			added = self.chain.add(block)
			if added:
				self.announceNewBlock()


	def announceNewBlock(self):
		for peer in self.network.nodes:
			if peer is not self:
				peer.consensus(self.chain)


	def consensus(self, chain):
		
		# TODO: better consensus - i think this is where proof of work check goes
		newLength = chain.length()
		currentLength = 0 if self.chain == None else self.chain.length()
		if newLength > currentLength and Blockchain.isValidChain(chain):
			self.chain = chain
			return True
		return False


	def __repr__(self):
		return self.name