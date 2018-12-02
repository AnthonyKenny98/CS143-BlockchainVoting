from election import Candidate, Voter, Vote
from network import Network

from random import randint, choice

nCandidates = 3
nVoters = 20
nNodes = 5

candidates = [Candidate("Candidate %s" % i) for i in range(nCandidates)]
voters = [Voter("Voter %s" % i) for i in range(nVoters)]

# Basic Simulation - no malicious activity

print("\n\nBasic Simulation - no malicious activity\n" + \
		  "========================================")

network = Network()
for i in range(nNodes):
	network.addNode()

print("Election with {} candidates and {} voters".format(nCandidates, nVoters))
print("Network with nodes: {}".format(network.nodes))

print("\nBEGIN ELECTION")

for voter in voters:
	node = network.nodes[randint(0,nNodes-1)]
	candidate = choice(candidates)
	vote = Vote(voter, candidate)
	print("{} goes to node {} and chooses to vote for candidate {}".format(voter, node, candidate))

	node.castVote(vote)

for node in network.nodes:
	print("{} last block is {} and is {} long".format(node, node.chain.last, node.chain.length))

print("\n\n")