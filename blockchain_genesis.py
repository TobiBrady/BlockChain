import hashlib as hasher
import datetime as date
import pickle

class Block:
    def __init__ (self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
            sha = hasher.sha256()
            sha.update(str(self.index) + 
                                 str(self.timestamp) + 
                                 str(self.data) + 
                                 str(self.previous_hash))
            return sha.hexdigest()

def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")

blockchain = [create_genesis_block()]

with open("blockchain_store.txt", "wb") as save:
	pickle.dump(blockchain, save)

print blockchain

print "\nGenisis block generated.\n"