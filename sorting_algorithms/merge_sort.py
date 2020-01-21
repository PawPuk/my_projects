class MergeSort():
	def __init__(self, list_to_sort):
		self.list_to_sort = list_to_sort
		self.sorted_list = None

	@staticmethod
	def split(list_to_split):
		split_index = len(list_to_split)//2
		# the second list in output is longer
		return list_to_split[:split_index], list_to_split[split_index:]

	@staticmethod
	def merge(list1, list2):
		merged_list = []
		while len(list1) > 0 and len(list2) > 0:
			# if we change <= to < we will get not stable algorithm
			if list1[0] <= list2[0]:
				merged_list.append(list1[0])
				list1 = list1[1:]
			else:
				merged_list.append(list2[0])
				list2 = list2[1:]
		if len(list1) > 0:
			merged_list.extend(list1)
		elif len(list2) > 0:
			merged_list.extend(list2)
		return merged_list

	def recursively_sort(self, list_to_sort):
		# recursive step
		if len(list_to_sort) > 1:
			left_sublist, right_sublist = self.split(list_to_sort)
			left_sublist = self.recursively_sort(left_sublist)
			right_sublist = self.recursively_sort(right_sublist)
			return self.merge(left_sublist, right_sublist)
		# base case
		return list_to_sort
	
	def sort(self):
		self.sorted_list = self.recursively_sort(self.list_to_sort)


# the following is example. Further tests shall be implemented
myObject = MergeSort([2, 4, 7, 2, 1, 19, 28, 14, 12, 6, 0, -2])
myObject.sort()
print()
print(myObject.sorted_list)
