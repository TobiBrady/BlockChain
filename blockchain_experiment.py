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

def next_block(last_block):
    this_index = blockchain.index(last_block) + 1
    this_timestamp = date.datetime.now()
    this_data = raw_input("\nBlock #" + str(this_index) + " data: \n")
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

def isint(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

with open("blockchain_store.txt", "rb") as stored_blockchain:
    progression = pickle.load(stored_blockchain)

blockchain = progression
print blockchain
previous_block = blockchain[len(blockchain) - 1]
print previous_block

commands = ["New", "All", "Recent", "Exit"]
commands_lower = [option.lower().replace(" ", "") for option in commands]
commands_description = ["adds a new block to the blockchain", "prints out the whole blockchain", 
                                                "prints out the recent bocks", "Exits the program"]

while True:
    while True:
        print "\nEnter a command from the list: "
        for (option, description) in zip(commands, commands_description):
            print str(commands.index(option) + 1) + ": " + str(option) + " (" + str(description) + ") "
        list_choice = raw_input("\nInput: ").lower().replace(" ", "")
        if list_choice not in commands_lower:
            print "\nUnrecognised command."
        else:
            print "\nCommand accepted."
            break

    if list_choice == commands_lower[0]:
        leave_new = 0
        while leave_new == 0 :
            block_to_add = next_block(previous_block)
            blockchain.append(block_to_add)
            previous_block = block_to_add
            print "\nBlock #{} has been added to the blockchain!".format(block_to_add.index)
            print "Hash: {}\n".format(block_to_add.hash)
            while True:
                answers = ["yes", "no"]
                another_block = raw_input("\nWould you like to add another block: ").lower()
                if another_block not in answers:
                    print "\nInvalid input"
                else:
                    if another_block == "yes":
                        break
                    else:
                        leave_new += 1
                        break

    elif list_choice == commands_lower[1]:
        for entry in blockchain:
            print str(entry.hash) + "\n"

    elif list_choice == commands_lower[2]:
        while True:
            blocks_to_print = raw_input("\nPrint how many recent blocks: ")
            if isint(blocks_to_print):
                break
            else:
                print "\nInvalid entry. Please input a whole number"
        for entry in blockchain[blockchain.index(block_to_add) - int(blocks_to_print): blockchain.index(block_to_add)]:
            print str(entry.hash) + "\n"

    elif list_choice == commands_lower[3]:
        print "\nExiting program"
        with open("blockchain_store.txt", "wb") as save:
            pickle.dump(blockchain, save)
            print "Updates saved\n"
        break