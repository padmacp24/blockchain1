import pytest
from test import ChainBlock, Blockchain

def test_create_block():
    t1 = "Rachel sends 5 Coin to Ross"
    t2 = "Ross sends 2.3 Coin to Monica"
    t3 = "Monica sends 4.2 Coin to Chandler"
    t4 = "Chandler sends 1.1 Coin to Joey"

    block1 = ChainBlock('firstblock', [t1, t2])
    print(f"Block 1 data: {block1.block_data}")
    print(f"Block 1 hash: {block1.block_hash}")

    block2 = ChainBlock(block1.block_hash, [t3, t4])
    print(f"Block 2 data: {block2.block_data}")
    print(f"Block 2 hash: {block2.block_hash}")

    if block1.block_hash in block2.block_data:
        print("The chaining is successful")
    else:
        raise Exception("The chaining is not successful")

def test_chaining():
    t1 = "George sends 3.1 GC to Joe"
    t2 = "Joe sends 2.5 GC to Adam"
    t3 = "Adam sends 1.2 GC to Bob"
    t4 = "Bob sends 0.5 GC to Charlie"
    t5 = "Charlie sends 0.2 GC to David"
    t6 = "David sends 0.1 GC to Eric"

    myblockchain = Blockchain()

    myblockchain.create_block_from_transaction([t1, t2])
    myblockchain.create_block_from_transaction([t3, t4])
    myblockchain.create_block_from_transaction([t5, t6])

    myblockchain.display_chain()