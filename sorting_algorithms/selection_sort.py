import argparse
import matplotlib.pyplot as plt
import numpy as np

class SelectionSort():
	"""
	A class used to sort the input list using Selection Sort algorithm

	...

	Attributes
	----------
	frame_rate : float
		decimal number expressing the frame rate of the graph
	input_list : list
		list to be sorted consisting of integers (no other data type allowed)
	output_list : list
		sorted version of input_list

	Methods
	-------
	find_minimal()
		Finds the minimal element in the input_list
	find_maximal()
		Finds the maximal element in the input_list
	sort()
		Moves the elements from input_list to output_list while making sure that they are sorted
	illustrate(maximal)
		Plots the input and output list on a bar graph (maximal is used to define the range of y axis)
	"""
	def __init__(self, list_to_be_sorted):
		self.frame_rate = 0.15
		self.input_list = []
		for element in list_to_be_sorted:
			self.input_list.append(int(element))
		self.output_list = None

	def find_maximal(self):
		maximal = None
		for element in self.input_list:
			if maximal == None:
				maximal = element
			elif element > maximal:
				maximal = element
		return maximal

	def find_minimal(self):
		minimal = None
		for element in self.input_list:
			if minimal == None:
				minimal = element
			# if we transform < to <= then we don't get a stable sorting algorithm
			elif element < minimal:
				minimal = element
		return minimal

	def illustrate(self, maximal):
		plt.clf()
		list_to_display1 = self.input_list
		list_to_display2 = self.output_list
		plt.subplot(121)
		plt.bar(np.arange(len(self.input_list)), self.input_list)
		axes = plt.gca()
		axes.set_ylim([0, maximal + 0.2*maximal])
		plt.subplot(122)
		plt.bar(np.arange(len(self.output_list)), self.output_list)
		axes = plt.gca()
		axes.set_ylim([0, maximal + 0.2*maximal])
		plt.show(block=False)
		plt.pause(self.frame_rate)

	def sort(self):
		self.output_list = []
		maximal = self.find_maximal()
		while len(self.input_list) > 0:
			self.illustrate(maximal)
			minimal_in_this_iteration = self.find_minimal()
			self.output_list.append(minimal_in_this_iteration)
			self.input_list.remove(minimal_in_this_iteration)
		self.illustrate(maximal)
		plt.show()


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("input_list", nargs='+', help="List to be sorted")
	args = parser.parse_args()
	selectionSort = SelectionSort(args.input_list)
	selectionSort.sort()
