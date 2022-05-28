import numpy as np
from mutator import Mutator
from loss_counter import LossCounter

class Population:
	def __init__(self, settings, shape, count):
		self.__settings = settings
		self.__population = []
		self.__mutator = Mutator()
		self.__loss_counter = LossCounter()
		for i in range(count):
			self.__population.append(np.random.randint(0,256,shape,dtype=np.uint8))

	def next(self, target):
		loss_value = self.__loss_sort(target)
		survivors_num = self.__settings.get_survivors_number()
		children_num = self.__settings.get_children_number()
		new_size = children_num * survivors_num + survivors_num;
		if new_size != len(self.__population):
			new_population = self.__population[:survivors_num]
			for i in range(survivors_num, new_size):
				new_population.append(None)
			self.__population = new_population
		for i in range(children_num):
			for survivor in range(survivors_num):
				self.__population[survivors_num+survivor*children_num+i] = self.__get_son(self.__population[survivor])
		return self.__population[0], loss_value

	def __loss_sort(self, target):
		losses = []
		for curr in range(len(self.__population)):
			losses.append([curr, self.__loss_counter.get_loss(self.__settings.get_loss_function(), target/256, self.__population[curr]/256)])
		losses.sort(key = lambda x: x[1])
		new_gen = []
		for i in losses:
			new_gen.append(self.__population[i[0]])
		self.__population = new_gen
		return losses[0][1]

	def __get_son(self, parent):
		son = np.copy(parent)
		for i in range(np.random.randint(1,self.__settings.get_changes_number()+1)):
			scale = np.random.randint(self.__settings.get_changes_scale())
			self.__mutator.make_mutation(self.__settings.get_mutation_type(), son, scale)
		return son