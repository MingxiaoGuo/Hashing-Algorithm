
import hashlib,json
from collections import OrderedDict

class MerkleTree:
	def __init__(self, transaction_list=None):
		self.transaction_list = transaction_list
		self.past_transaction = OrderedDict()
	
	def create_tree(self):
		transaction_list = self.transaction_list
		past_transaction = self.past_transaction

		temp_transaction = []
		is_right_empty = False

		for index in range(1, len(transaction_list), 2):
			current_node = transaction_list[index]

			if index + 1 != len(transaction_list):
				right_node = transaction_list[index + 1]
			else:
				is_right_empty = True
				right_node = ''

			current_hash = hashlib.sha256(current_node.encode('utf-8'))
			if is_right_empty == False:
				right_hash = hashlib.sha256(right_node.encode('utf-8'))

			past_transaction[current_node] = current_hash.hexdigest()
			if is_right_empty == False:
				past_transaction[right_node] = right_hash.hexdigest()

			if is_right_empty == False:
				temp_transaction.append(current_hash.hexdigest() + right_hash.hexdigest())
			else:
				temp_transaction.append(current_hash.hexdigest())

		if len(transaction_list) != 1:
			self.transaction_list = temp_transaction
			self.past_transaction = past_transaction
			self.create_tree()

	def get_past_transacion(self):
		return self.past_transaction

	def get_Root_leaf(self):
		last_key = self.past_transaction.keys()[-1]
		return self.past_transaction[last_key]

if __name__ == '__main__':
	tree = MerkleTree()

	transactions = ['a', 'b', 'c', 'd']

	tree.transaction_list = transactions
	tree.create_tree()

	past_transaction = tree.get_past_transacion()
	print(json.dumps(past_transaction, indent=4))
	print ("-" * 50 )
