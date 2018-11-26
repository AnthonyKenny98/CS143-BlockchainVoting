import time

class Block:
    def __init__(self, data, prev):
        self.time = time.time()
        self.data = data
        self.prev = prev
