import numpy as np
from mutator import Mutator
from loss_counter import LossCounter
import random

class Population:
	def __init__(self, settings, shape, count):
		self.__settings = settings
		self.__population = []
		self.__mutator = Mutator()
		self.__loss_counter = LossCounter()
		for i in range(count):
			self.__population.append(np.random.randint(0,256,shape,dtype=np.uint8))

	def get_best_creature(self):
		return self.__population[0]

	def next(self, target):
		loss_value = self.__loss_sort(target)
		if self.__settings.is_single_parent():
			self.__single_parent_mode()
		else:
			self.__two_parent_mode()
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

	def __single_parent_mode(self):
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
				self.__population[survivors_num+survivor*children_num+i] = self.__get_son_single(self.__population[survivor])

	def __get_son_single(self, parent):
		son = np.copy(parent)
		for i in range(np.random.randint(1,self.__settings.get_changes_number()+1)):
			scale = np.random.randint(self.__settings.get_changes_scale())
			self.__mutator.make_mutation(self.__settings.get_mutation_type(), son, scale)
		return son

	def __two_parent_mode(self):
		children_num = self.__settings.get_children_number()
		new_size = children_num * 2 + 2;
		if new_size != len(self.__population):
			new_population = self.__population[:2]
			for i in range(2, new_size):
				new_population.append(None)
			self.__population = new_population
		for i in range(children_num):
			self.__population[2 + i] = self.__get_son_two(self.__population[:2])

	def __get_son_two(self, parents):
		bound = np.random.randint(1, parents[0].shape[0] - 1)
		son = np.concatenate((parents[0][:bound], parents[1][bound:]), axis=0)
		for i in range(np.random.randint(1,self.__settings.get_changes_number()+1)):
			scale = np.random.randint(self.__settings.get_changes_scale())
			self.__mutator.make_mutation(self.__settings.get_mutation_type(), son, scale)
		return son