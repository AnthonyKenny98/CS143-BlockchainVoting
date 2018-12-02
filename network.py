import time
from copy import copy
from random import randint

from blockchain import Blockchain
from block import Block
from election import Vote, Voter, Candidate


class Network(object):

	def __init__(self):
		self.nodes = []


	def addNode(self):
		newNode = Node(len(self.nodes), self)
		self.nodes.append(newNode)


class Node(object):

	def __init__(self, index, network):
		self.index = index
		self.name = "N{}".format(self.index)
		self.chain = None
		self.network = network
		if len(network.nodes) > 0:
			self.consensus

	def __repr__(self):
		return "node: {}".format(self.name)

	def addBlock(self, block):
		try:
			added = self.chain.add(block)
			if added:
				self.announceNewBlock()
		except Exception:
			self.chain = Blockchain([block])


	def announceNewBlock(self):
		for peer in self.network.nodes:
			if peer is not self:
				peer.consensus()

	def consensus(self):
		longestChain = None
		currentLength = 0 if self.chain == None else self.length()
		for node in self.network.nodes:
			if node is self:
				break
			chain = node.chain
			chainLength = chain.length()
			if chainLength > currentLength and Blockchain.isValidChain(chain):
				currentLength = chainLength
				longestChain = chain
			if longestChain:
				self.chain = longestChain
				return True
		return False