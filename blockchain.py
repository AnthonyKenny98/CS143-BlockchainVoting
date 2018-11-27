
class Blockchain:
    def __init__(self, genesis):
        self.blocks = set([(genesis.sha256(), genesis, 0)])

    def add(self, block):
        prevdepth = self.check(block)

        if prevdepth != None:
            self.blocks.add((block.sha256(), block, prevdepth + 1))
            return True
        else:
            return False

    def check(self, block):
        def hashset(hashables):
            return frozenset(map(lambda x: x.sha256(), hashables))

        prevhash = block.prev
        prevdepth = None

        while prevhash != None:
            try:
                prevblock = filter(lambda b: b[0] == prevhash, self.blocks)[0]

                hashes = hashset(block.data)
                len0 = len(block.data)
                len1 = len(hashes)
                len2 = len(prevblock[1].data)
                len3 = len(hashset(prevblock[1].data) - hashes)

                if len0 == len1 and len2 == len3:
                    prevhash = prevblock[1].prev

                    if prevdepth == None:
                        prevdepth = prevblock[2]
                else:
                    return None
            except IndexError:
                return None

        return prevdepth

    def last(self):
        return max(self.blocks, key = lambda b: b[2])

