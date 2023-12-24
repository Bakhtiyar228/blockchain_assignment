# main.py
from flask import Flask, render_template, request
from functions import generate_keypair, encrypt, decrypt, sign_message, verify_signature, Block
from merkle_tree import MerkleTree

app = Flask(__name__)

blockchain = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    p = int(request.form['p'])
    q = int(request.form['q'])
    plaintext = request.form['plaintext']

    public_key, private_key = generate_keypair(p, q)
    signature = sign_message(private_key, plaintext)
    ciphertext = encrypt(public_key, plaintext)
    decrypted_message = decrypt(private_key, ciphertext)
    is_signature_valid = verify_signature(public_key, decrypted_message, signature)

    # Blocks of Blockchain
    block = Block(public_key, plaintext, signature, ciphertext, decrypted_message, is_signature_valid)
    blockchain.append(block)

    # Merkle tree
    transaction_data = [(block.public_key, block.plaintext, block.signature, block.ciphertext, block.decrypted_message,
                         block.is_signature_valid) for block in blockchain]
    merkle_tree = MerkleTree(transaction_data)
    merkle_root = merkle_tree.get_root()

    return render_template('result.html', block=block, merkle_root=merkle_root)


if __name__ == '__main__':
    app.run(debug=True)
