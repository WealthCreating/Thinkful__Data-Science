'''
Implement a binary tree, which is filled with 15 pieces of random data.
Your job is to then write a program to traverse the tree using a breadth first traversal.
'''
import random

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

random_list = list(random.sample(range(100), 15))

root = Node(random_list[0])

for i in random_list[1:]:
	root.insert(i)

root.PrintTree()
