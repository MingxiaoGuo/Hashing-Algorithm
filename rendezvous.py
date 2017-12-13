import hashlib

class RendezvousHash(object):
    """This class implements the Rendezvous (HRW) hashing logic."""

    def __init__(self, nodes=None):
        # TODO
        self.nodes = nodes
        
    
    def get_node(self, key):
        # TODO
        highest_node = None
        hash_result = {}
        for x in self.nodes:
            temp_str = (x + key).encode('utf-8')
            hash_val = hashlib.md5(temp_str).hexdigest()
            hash_result[hash_val] = x
        
        highest_key = list(hash_result.keys())[0]
        highest_node = hash_result[highest_key]
        return highest_node

def test():
  rendezvousHash = RendezvousHash(['0.0.0.0:3000', '0.0.0.0:3001', '0.0.0.0:3002'])
  keys = ['Good', 'luck', 'in', 'your', 'exam']
  for key in keys:
    node = rendezvousHash.get_node(key)
    print("'{}' is mapped to node: {}".format(key, node))
    
test()

