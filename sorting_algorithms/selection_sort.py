class SelectionSort():
	def __init__(self, list_to_be_sorted):
		self.list_to_sort = list_to_be_sorted
		self.sorted_list = None

	def find_minimal(self):
		minimal = None
		for element in self.list_to_sort:
			if minimal == None:
				minimal = element
			# if we transform < to <= then we get not stable sorting algorithm
			elif element < minimal:
				minimal = element
		return minimal

	# after calling this method self.sorted_list contains sorted list and self.list_to_sort is empty
	def sort(self):
		self.sorted_list = []
		while len(self.list_to_sort) > 0:
			minimal_in_this_iteration = self.find_minimal()
			self.sorted_list.append(minimal_in_this_iteration)
			self.list_to_sort.remove(minimal_in_this_iteration)


# the following is example. Further tests shall be implemented
myObject = SelectionSort([2, 4, 7, 2, 1, 19, 28, 14, 12, 6, 0, -2])
print(myObject.list_to_sort)
print(myObject.sorted_list)
myObject.sort()
print(myObject.list_to_sort)
print(myObject.sorted_list)

