from flask import Flask, request
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


# Instantiate the blockchain
blockchain = Blockchain()

# Instantiate the Flask app
app = Flask(__name__)

# Define the routes
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    # Check that the required fields are in the POST'ed data
    required = ['sender', 'receiver', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400

    # Create a new transaction
    response = blockchain.create_transaction(values['sender'], values['receiver'], values['amount'])
    return response, 201

@app.route('/mine', methods=['GET'])
def mine():
    # Mine a new block
    response = blockchain.mine_block()
    return response, 200

@app.route('/chain', methods=['GET'])
def full_chain():
    # Return the full blockchain
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return json.dumps(response), 200

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
