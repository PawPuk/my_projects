class LinkedList():
	def __init__(self, node=None):
		self.head = node
	
	# zero-based index
	def insert(self, index, node_to_insert):
		if index == 0:
			node_to_insert.next = self.head
			self.head = node_to_insert
		elif index > 0:
			current_node = self.head
			current_index = index
			while current_index > 1 and current_node.next is not None:
				current_index -= 1
				current_node = current_node.next
			if current_node.next is not None:
				(current_node.next).previous = node_to_insert
				node_to_insert.next = current_node.next
				node_to_insert.previous = current_node
				current_node.next = node_to_insert
			else:
				node_to_insert.next = current_node.next
				node_to_insert.previous = current_node
				current_node.next = node_to_insert
		else:
			raise ValueError
	
	#zero-based index
	def remove(self, index):
		if index == 0:
			self.head = (self.head).next
			self.head.previous = None
		elif index > 0:
			current_node = self.head
			current_index = index
#			1 -> 2 -> 3 -> None
			while current_index > 1 and (current_node.next).next is not None:
				current_index -= 1
				current_node = current_node.next
			current_node.next = (current_node.next).next
			if current_node.next is not None:
				(current_node.next).previous = current_node
		else:
			raise ValueError
	
	def __str__(self):
		return str("None <--> " + str(self.head))


class Node():
	def __init__(self, value, next=None, previous=None):
		self.value = value
		self.next = next
		self.previous = previous

	def __str__(self):
		return str(self.value) + " <--> " + str(self.next)


linked_list = LinkedList(Node(0))
linked_list.insert(15, Node(2))
linked_list.insert(1, Node(1))
linked_list.insert(0, Node(-1))
print(linked_list)
linked_list.remove(2)
print(linked_list)

