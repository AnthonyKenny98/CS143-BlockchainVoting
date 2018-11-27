import hashlib
import pickle
import time

class Hashable:
    def __init__(self):
        pass

    def sha256(self):
        return hashlib.sha256(pickle.dumps(self)).hexdigest()

class Block(Hashable):
    def __init__(self, data, prev):
        self.time = time.time()
        self.data = data
        self.prev = prev

class Vote(Hashable):
    def __init__(self, voter, candidate):
        self.voter = voter
        self.candidate = candidate

    def sha256(self):
        return hashlib.sha256(self.voter).hexdigest()
