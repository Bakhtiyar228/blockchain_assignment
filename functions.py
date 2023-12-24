import hashlib

def generate_keypair(p, q, e=29):
    n = p * q
    z = (p - 1) * (q - 1)
    d = pow(e, -1, z)
    public_key = (n, e)
    private_key = (n, d)
    return public_key, private_key

def encrypt(public_key, plaintext):
    n, e = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    n, d = private_key
    decrypted_values = [pow(char, d, n) for char in ciphertext]
    decrypted_message = ''.join([chr(val) for val in decrypted_values])
    return decrypted_message

def simple_hash(message):
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))
    return int(sha256.hexdigest(), 16)

def sign_message(private_key, message):
    n, d = private_key
    hash_value = simple_hash(message)
    signature = pow(hash_value, d, n)
    return signature

def verify_signature(public_key, message, received_signature):
    n, e = public_key
    computed_hash = pow(received_signature, e, n)
    return computed_hash == simple_hash(message) % n

class Block:
    def __init__(self, public_key, plaintext, signature, ciphertext, decrypted_message, is_signature_valid):
        self.public_key = public_key
        self.plaintext = plaintext
        self.signature = signature
        self.ciphertext = ciphertext
        self.decrypted_message = decrypted_message
        self.is_signature_valid = is_signature_valid

    def __str__(self):
        return f"Block(public_key={self.public_key}, plaintext={self.plaintext}, signature={self.signature}, ciphertext={self.ciphertext}, decrypted_message={self.decrypted_message}, is_signature_valid={self.is_signature_valid})"
