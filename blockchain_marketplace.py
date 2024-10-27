import hashlib
import time

class Transaction:
    def __init__(self, sender, recipient, amount, timestamp = None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = timestamp if timestamp else time.time()

    def to_dict(self):
        return{
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount,
            "timestamp": self.timestamp
        }
    

class Block:
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Concatenate block attributes and hash them
        data_string = str(self.index) + self.previous_hash + str(self.timestamp) + str(self.data)
        return hashlib.sha256(data_string.encode()).hexdigest()
    
    def to_dict(self):
        return{
            "index": self.index,
            "previous_hash": self.previous_hash,
            "timestamp": self.timestamp,
            "data": self.data,
            "hash": self.hash
        }
    

class Blockchain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "0", time.time(), [])
        self.chain.append(genesis_block)

    def add_block(self, block):
        if block.previous_hash != self.chain[-1].hash:
            return False     #Block is Invalid
        self.chain.append(block)
        return True
    
    def get_latest_block(self):
        return self.chain[-1] if self.chain else None
    
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chsin[i - 1]
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
    

class SmartContract:
    def __init__(self, contract_id, owner, balance = 0):
        self.contract_id = contract_id
        self.owner = owner
        self.balance = balance

    def transfer(self, amount, recipient):
        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            return True
        return False
    
    def deposit(self, amount):
        self.balance += amount


class User:
    def __init__(self, user_id, balance = 0):
        self.user_id = user_id
        self.balance = balance

    def send_transaction(self, recipient, amount):
        if self.balance >= amount:
            transaction = Transaction(self.user_id, recipient.user_id, amount)
            self.balance -= amount
            recipient.balance += amount
            return transaction
        return None   # Insufficient funds
    
def mine_block(block):
    block.hash = block.calculate_hash()


if __name__ == "__main__":
    # Initialize blockchain
    blockchain = Blockchain()
    print("Blockchain initialized. ")

    user1 = User("Mahir", 100)
    user2 = User("Mala", 50)


    # User1 sends transaction to User2
    transaction1 = user1.send_transaction(user2, 30)
    if transaction1:
        blockchain.pending_transactions.append(transaction1)


    # Mine and add a block with pending transactions
    new_block = Block(len(blockchain.chain), blockchain.get_latest_block().hash, time.time(), blockchain.pending_transactions)
    mine_block(new_block)
    blockchain.add_block(new_block)
    print("New block mined and added.")


    # Display blockchain data
    for block in blockchain.chain:
        print(f"Block {block.index}: {[tx.to_dict() for tx in block.data]}, Hash: {block.hash}")