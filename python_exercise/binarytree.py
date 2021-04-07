class Node(object):
	def __init__(self, value):
		self.value = value 
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def search(self, find_val):
		return self.preorder_search(tree.root, find_val)

	def print_tree(self):
		return self.preorder_print(tree.root, "")[:-1]

	def preorder_search(self, start, find_val):
		if start: # Not None 
			if start.value == find_val:
			#if start.left == find_val:
				return True
			else:
				# recursively find the children of the current node 
				return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)

		return False

	#def preorder_print(self, start, traversal):
	#	if start:
	#		traversal += (str(start.value) + "-")
	#		tracersal = self.preorder_print(start.left, traversal)
	#		traversal = self.preorder_print(start.right, traversal)
	#	return traversal

	def preorder_print(self, start, traversal):
        #if start:
        if start:
        	traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

tree = BinaryTree(1)
#tree.root.left = Node(2)
tree.root.left = Node(2)
tree.root.right = Node(3)

#tree.root.left.left = Node(4)
tree.root.left.left = Node(4)

#tree.root.left.right = Node(5)
tree.root.left.right = Node(5)


# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))

# should print 1-2-4-5-3
print(tree.print_tree())

