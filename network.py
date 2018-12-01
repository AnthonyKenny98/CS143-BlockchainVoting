class Chain(object):

	def __init__(self, length):
		self.length = length

	def add(self):
		self.length += 1
		return True

	@staticmethod
	def isValidChain(chain):
		return True

class Node(object):

	def __init__(self, index):
		self.index = index
		self.name = "N{}".format(self.index)
		self.chain = Chain(0)
		self.peers = []

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
	# create nodes
	
	frames = []
	n = 10
	nodes = [Node(i) for i in range(n)]
	assert len(nodes) == n
	
	# add peers to each node
	for node in nodes:
		node.peers = list(filter(lambda x: x is not node,nodes))
		assert len(node.peers) == n-1

	nodes[0].addBlock()
	for node in nodes:
		assert node.chain.length == 1

if __name__ == '__main__':
	
	simpleSimulation()
