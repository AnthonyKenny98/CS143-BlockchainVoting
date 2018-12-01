class Candidate:

	def __init__(self, name, party=None):
		self.name = name
		self.party = party

	def __repr__(self):
		return self.name
