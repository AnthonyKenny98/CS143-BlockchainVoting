class Election(object):
	""" Represents the election that is being run."""

	def __init__(self, candidates):
		self.candidates = candidates
	

class Candidate(object):
	""" Represents a candidate that can be voted for."""
	
	def __init__(self, name):
		"""Create a new candidate. Contains:
			name
		"""
		
		self.name = name

	def __repr__(self):
		return self.name
	

class Voter(object):
	""" Represents an eligible voter """

	def __init__(self, name):
		"""Create a new candidate. Contains:
			name
		"""
		self.name = name

	def __repr__(self):
		return self.name


class Vote(tuple):
    """Represent who voted for whom in a simple class object."""

    def __new__(self, voter, candidate):
        """Create a new tuple containing the name of both the voter and the
        candidate for whom she voted.
        """

        return tuple.__new__(self, (voter, candidate))

    @property
    def voter(self):
        """Return the voter's name."""
        return tuple.__getitem__(self, 0)