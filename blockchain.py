from block import Block

class Blockchain:
    def __init__(self, genesis):
        self.blocks = set([(hash(genesis), genesis, 0)])

    def add(self, block):
        pass

    def check(self, block):
        prevhash = block.prev

        while prevhash != None:
            try:
                prevblock = filter(lambda b: b[0] == prevhash, self.blocks)[0][1]

                len0 = len(prevblock.data)
                len1 = len(prevblock.data - block.data)

                if len0 == len1:
                    prevhash = prevblock.prev
                else:
                    return False
            except IndexError:
                return False
        return True

    def last(self):
        return max(self.blocks, key = lambda b: b[2])

