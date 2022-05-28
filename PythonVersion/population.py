import numpy as np
from mutation import *

class Population:
	def __init__(self, settings, shape, count):
		self.__settings = settings
		self.__population = []
		for i in range(count):
			self.__population.append(np.random.randint(0,256,shape,dtype=np.uint8))

	def get_best(self):
		return self.__population[0]

	def next(self, target):
		self.__loss_sort(target)
		new_size = self.__settings.get_sons_number() * 2 + 2;
		if new_size != len(self.__population):
			new_population = [self.__population[0], self.__population[1]]
			for i in range(2, new_size):
				new_population.append(None)
			self.__population = new_population
		for i in range(self.__settings.get_sons_number()):
			self.__population[2+i] = self.__get_son(self.__population[0])
			self.__population[2+self.__settings.get_sons_number()+i] = self.__get_son(self.__population[1])

	def __loss_sort(self, target):
		losses = []
		for curr in range(len(self.__population)):
			losses.append([curr, self.__loss(target/256, self.__population[curr]/256)])
		losses.sort(key = lambda x: x[1])
		print(losses[0][1])
		new_gen = []
		for i in losses:
			new_gen.append(self.__population[i[0]])
		self.__population = new_gen

	def __loss(self, target, pred):
		diff = pred - target
		differences_squared = diff ** 2
		mean_diff = differences_squared.mean()
		return mean_diff

	def __get_son(self, parent):
		son = np.copy(parent)
		for i in range(np.random.randint(1,self.__settings.get_changes_number()+1)):
			scale = np.random.randint(self.__settings.get_changes_scale())
			mutation(self.__settings.get_mutation_type(), son, scale)
		return son