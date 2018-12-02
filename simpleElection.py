import unittest
from random import randint, choice

from election import Candidate, Voter, Vote
from network import Network

class SimpleElection(unittest.TestCase):
    """Simple, non malicious election to test functionality"""

    def setUp(self):

    	self.nCandidates = 3
    	self.nVoters = 10
    	self.nNodes = 5

    	self.candidates = [Candidate("Candidate %s" % i) for i in range(self.nCandidates)]
    	self.voters = [Voter("Voter %s" % i) for i in range(self.nVoters)]

    	self.network = Network()
    	for i in range(self.nNodes):
    		self.network.addNode()

    def test_ElectionSetup(self):
        """Ensure that the only time that two blocks have the same hash is when
        the two blocks are the same block (i.e. all attributes are the same).
        """

        print("\n\n#### TEST SETUP OF SIMPLE ELECTION ####\n")

        self.assertEqual(len(self.candidates), self.nCandidates)
        self.assertEqual(len(self.voters), self.nVoters)
        self.assertEqual(len(self.network.nodes), self.nNodes)
       
        print("TEST 1 PASSED\n=============")
        print("Election Set Up Successful:\n" + \
        		"    Candidates = {}\n".format(self.nCandidates) + \
        		"    Voters = {}\n".format(self.nVoters) + \
        		"    Nodes = {}".format(self.nNodes))

    def test_RunElection(self):

    	print("\n\n#### COMMENCE VOTING ####\n")

    	for voter in self.voters:
    		node = self.network.nodes[randint(0,self.nNodes-1)]
    		candidate = choice(self.candidates)
    		vote = Vote(voter, candidate)
    		print("{} goes to node {} and chooses to vote for candidate {}".format(voter, node, candidate))

    		self.assertEqual(node.castVote(vote), True)

    	print("\n\n#### COMPARING EACH NODE'S CHAIN ####\n")

    	for i in range(self.nNodes):
    		for j in range(self.nNodes):
    			if i != j:
		    		self.assertEqual(self.network.nodes[i].chain, self.network.nodes[j].chain)
		    		print("{} == {}".format(self.network.nodes[i], self.network.nodes[j]))

    	print("\nTEST 2 PASSED\n=============")
    	print("{} votes successfully cast".format(self.nVoters))
    	print("All nodes have equal chains\n".format(self.nVoters))


if __name__ == '__main__':
    unittest.main()