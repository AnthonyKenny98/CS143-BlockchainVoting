import time
from copy import copy
from random import randint

from nodeServer import Node, NaughtyNode


class Network(object):

	def __init__(self):
		self.nodes = []

	def addNode(self):
		newNode = Node(len(self.nodes), self)
		self.nodes.append(newNode)

	def addBadNode(self):
		newNode = NaughtyNode(len(self.nodes), self)
		self.nodes.append(newNode)