'''
Implement a binary tree, which is filled with 15 pieces of random data.
Your job is to then write a program to traverse the tree using a breadth first traversal.
'''
import random

class Node:
	def __init__(self, val):
		self.left = None
		self.right = None
		self.value = val

class Tree:
	def __init__(self):
		self.root = None

	def get_root(self):
		return self.root

	def add(self, val):
		if self.root == None:
			self.root = Node(val)
		else:
			self._add(val, self.root)

	def _add(self, val, node):
		if val < node.value:
			if not node.left:
				self._add(val, node.left)
			else:
				node.left = Node(val)

		else:
			if not node.right:
				self._add(val, node.right)
			else:
				node.right = Node(val)

	def find(self, val):
		if not self.root:
			return self._find(val, self.root)
		else:
			return

	def _find(self, val, node):
		if val == node.value:
			return node
		elif val < node.value and not node.left:
			self._find(val, node.left)
		elif val > node.value and not node.right:
			self._find(val, node.r)

	def printTree(self):
		if not self.root:
			self._printTree(self.root)

	def _printTree(self, node):
		if not node:
			self._printTree(node.left)
			print(node.value + ' ')
			self._printTree(node.right)


tree = Tree()
random_list = list(random.sample(range(100), 15))

for i in random_list:
	tree.add(i)
