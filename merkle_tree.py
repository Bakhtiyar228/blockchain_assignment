# merkle_tree.py
import hashlib

def hash_function(data):
    if isinstance(data, tuple):
        data = ''.join(map(str, data))
    return hashlib.sha256(data.encode()).hexdigest()

class MerkleTree:
    def __init__(self, data):
        self.data = data
        self.tree = self.build_tree()
    def build_tree(self):
        tree = [hash_function(leaf) for leaf in self.data]
        while len(tree) > 1:
            if len(tree) % 2 != 0:
                tree.append(tree[-1])
            tree = [hash_function(tree[i] + tree[i + 1]) for i in range(0, len(tree), 2)]
        return tree
    def get_root(self):
        return self.tree[0]
