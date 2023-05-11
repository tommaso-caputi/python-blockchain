import json
import hashlib

class Blockchain():
    def __init__(self):
        self.chain = [{}]
        self.unconfirmed_transactions = []

    def create_transaction(self,sender, receiver, amount):
        self.unconfirmed_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return 'New transaction shared'
    
    def create_block(self, proof):
        self.chain.append({
            'index': len(self.chain)+1,
            'transactions': self.unconfirmed_transactions,
            'proof': proof,
            'previous_hash': self.hash(self.chain[-1]),
        })
        self.unconfirmed_blocks = []
        return 'New block generated'
    
    

    def hash(self, block):   
        json_str = json.dumps(block, sort_keys=True).encode('utf-8') # Sort the keys for consistency
        hash_obj = hashlib.sha256(json_str)
        hash_value = hash_obj.hexdigest()
        return hash_value


blockchain = Blockchain()
blockchain.create_transaction('send','rec','5')
blockchain.create_transaction('send','rec','7')
blockchain.create_block(10)
print(blockchain.chain)