import json
import hashlib

class Blockchain():
    def __init__(self):
        self.chain = [{}]
        self.unconfirmed_transactions = []
        self.difficulty=1

    def create_transaction(self,sender, receiver, amount):
        self.unconfirmed_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return 'New transaction shared'
    
    def mine_block(self):
        hash = 'casda'
        nonce = 0
        while not self.check_valid_hash(hash):
            nonce+=1
            block = {
                'index': len(self.chain)+1,
                'transactions': self.unconfirmed_transactions,
                'nonce': nonce,
                'previous_hash': self.hash(self.chain[-1]),
            }
            hash = self.hash(block)
        self.chain.append(block)
        self.unconfirmed_transactions = []
        return 'New block mined: '+str(self.chain[-1])

    def check_valid_hash(self, hash):
        if hash[:self.difficulty] == '0'*self.difficulty:
            return True 
        else:
            return False

    def hash(self, block):   
        json_str = json.dumps(block, sort_keys=True).encode('utf-8') # Sort the keys for consistency
        hash_obj = hashlib.sha256(json_str)
        hash_value = hash_obj.hexdigest()
        return hash_value

""" blockchain = Blockchain()
blockchain.create_transaction('send','rec','5')
blockchain.create_transaction('send','rec','7')
print(blockchain.mine_block())
blockchain.create_transaction('send','rec','1')
print(blockchain.mine_block())
print(blockchain.chain) """