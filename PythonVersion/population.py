import numpy as np

class Population:
	def __init__(self, shape, count):
		self.__population = []
		for i in range(count):
			self.__population.append(np.random.randint(0,256,shape,dtype=np.uint8))

	def get_best(self):
		return self.__population[0]

	def next(self, target):
		self.__loss_sort(target)
		for i in range(4):
			self.__population[2+i] = self.__get_son(self.__population[0])
			self.__population[6+i] = self.__get_son(self.__population[1])

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
		for i in range(np.random.randint(1,20)):
			#son[np.random.randint(parent.shape[0])][np.random.randint(parent.shape[1])][np.random.randint(parent.shape[2])] = np.random.randint(0,256)
			radius = np.random.randint(min(parent.shape[0] / 20, parent.shape[1] / 20))
			x = np.random.randint(parent.shape[0])
			y = np.random.randint(parent.shape[1])
			rgb = [np.random.randint(0,256), np.random.randint(0,256), np.random.randint(0,256)]
			for i in range (max(0, x - radius), min(parent.shape[0], x + radius)):
				for j in range (max(0, y - radius), min(parent.shape[1], y + radius)):
					son[i][j] = rgb
		return son