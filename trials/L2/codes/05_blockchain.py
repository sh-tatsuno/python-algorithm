import hashlib
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash = 0):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous_block = None

    def calc_hash(self):
        sha = hashlib.sha256()
        text = str(self.previous_hash) + str(self.timestamp) + str(self.data)
        hash_str = text.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

# implement blockchain with add_block & print_blockchain
class BlockChain():
    def __init__(self, timestamp, data):
        self.latest = Block(timestamp, data)

    def add_block(self):
        new_block = Block(self.latest.timestamp, self.latest.data, self.latest.hash)
        new_block.previous_block = self.latest
        self.latest = new_block

    def print_blockchain(self):
        current_block = self.latest
        while(True):
            if current_block == None:
                break
            print("""<Block> 
            timestamp: {0}
            data: {1}
            previous_hash: {2}
            hash: {3}
            """.format(current_block.timestamp, 
                    current_block.data, 
                    current_block.previous_hash, 
                    current_block.hash))
            current_block = current_block.previous_block

if __name__ == "__main__":
    ts = datetime.datetime(2014, 11, 9, 23, 21, 13, 99776)
    data = "hello algorithm!"
    blockchain = BlockChain(ts, data)

    # test 1
    # check when only one block
    print('test1')
    blockchain.print_blockchain()


    # test 2
    # check when two more (three) block
    print('test2')
    blockchain.add_block()
    blockchain.add_block()
    blockchain.print_blockchain()

    # test 3
    # check if when data are empty
    print('test3')
    data = ""
    blockchain = BlockChain(ts, data)
    blockchain.add_block()
    blockchain.print_blockchain()