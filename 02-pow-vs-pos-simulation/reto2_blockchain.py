import hashlib
import time
import random

class Block:
    def __init__(self, index, transactions, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, ["Genesis Block"], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

def mine_block(block, difficulty):
    start = time.time()
    while block.hash[:difficulty] != "0" * difficulty:
        block.nonce += 1
        block.hash = block.calculate_hash()
    end = time.time()
    print(f"PoW minado en {end - start:.4f} segundos")
    return block

validators = [
    {"name": "A", "stake": 50},
    {"name": "B", "stake": 30},
    {"name": "C", "stake": 20}
]

def select_validator(validators):
    total = sum(v["stake"] for v in validators)
    pick = random.uniform(0, total)
    current = 0
    for v in validators:
        current += v["stake"]
        if current > pick:
            return v

blockchain_pow = Blockchain()
blockchain_pos = Blockchain()

transactions = [
    ["A -> B: 10"],
    ["B -> C: 5"],
    ["C -> A: 2"]
]

difficulty = 4

print("=== SIMULACION PROOF OF WORK ===")

for i, tx in enumerate(transactions, start=1):
    block = Block(i, tx, blockchain_pow.get_latest_block().hash)
    mined_block = mine_block(block, difficulty)
    blockchain_pow.add_block(mined_block)
    print(f"Bloque {i} PoW validado")
    print(f"Nonce encontrado: {mined_block.nonce}")
    print(f"Hash: {mined_block.hash}")
    print("-" * 60)

print("\n=== SIMULACION PROOF OF STAKE ===")

for i, tx in enumerate(transactions, start=1):
    start = time.time()
    validator = select_validator(validators)
    block = Block(i, tx, blockchain_pos.get_latest_block().hash)
    block.hash = block.calculate_hash()
    blockchain_pos.add_block(block)
    end = time.time()

    print(f"Bloque {i} PoS validado")
    print(f"Validador elegido: {validator['name']}")
    print(f"Stake del validador: {validator['stake']}")
    print(f"Tiempo de validacion PoS: {end - start:.6f} segundos")
    print(f"Hash: {block.hash}")
    print("-" * 60)
