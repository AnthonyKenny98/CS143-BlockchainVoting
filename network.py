from copy import copy

class Chain(object):

	def __init__(self, length):
		self.length = length

	def add(self):
		self.length += 1
		return True

	@staticmethod
	def isValidChain(chain):
		return True

class Network(object):

	def __init__(self):
		self.nodes = []

	def addNode(self):
		newNode = Node(len(self.nodes), copy(self.nodes))
		for node in self.nodes:
			node.peers.append(newNode)
		self.nodes.append(newNode)
		
	def getLengths(self):
		lengths = []
		for node in self.nodes:
			lengths.append((node.index, node.chain.length))
		return lengths


class Node(object):

	def __init__(self, index, peers):
		self.index = index
		self.name = "N{}".format(self.index)
		self.chain = Chain(0)
		self.peers = peers

	def __repr__(self):
		return "node: {}, length: {}".format(self.name, self.chain.length)

	def addBlock(self):
		added = self.chain.add()
		if added:
			self.announceNewBlock()

	def announceNewBlock(self):
		for peer in self.peers:
			peer.consensus()

	def consensus(self):
		longestChain = None
		currentLength = self.chain.length
		for node in self.peers:
			chain = node.chain
			if chain.length > currentLength and Chain.isValidChain(chain):
				currentLength = chain.length
				longestChain = chain
			if longestChain:
				self.chain = longestChain
				return True
		return False


def simpleSimulation():
	n=10

	# init Network
	N = Network()

	# create nodes
	for _ in range(n):
		N.addNode()
	assert len(N.nodes) == n
	
	for node in N.nodes:
		assert len(node.peers) == n-1

	# nodes[0].addBloc8

if __name__ == '__main__':
	
	simpleSimulation()
