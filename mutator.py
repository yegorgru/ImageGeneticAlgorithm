import numpy as np
import random
import raster_geometry as rg

class Mutator:
	def make_mutation(self, type, creature, scale):
		if type == "Square":
			self.__square_mutation(creature, scale)
		elif type == "Line":
			self.__line_mutation(creature, scale)
		elif type == "Point":
			self.__point_mutation(creature, scale)
		elif type == "Triangle":
			self.__triangle_mutation(creature, scale)
		elif type == "Circle":
			self.__circle_mutation(creature, scale)
		else:
			raise Exception("Unknown mutation type")

	def __square_mutation(self, creature, scale):
		x = np.random.randint(creature.shape[0])
		y = np.random.randint(creature.shape[1])
		rgb = [np.random.randint(0,256), np.random.randint(0,256), np.random.randint(0,256)]
		for i in range (max(0, x - scale), min(creature.shape[0], x + scale)):
			for j in range (max(0, y - scale), min(creature.shape[1], y + scale)):
				creature[i][j] = rgb

	def __line_mutation(self, creature, scale):
		x = np.random.randint(creature.shape[0])
		y = np.random.randint(creature.shape[1])
		rgb = [np.random.randint(0,256), np.random.randint(0,256), np.random.randint(0,256)]
		horizontal = random.choice([True, False])
		if horizontal:
			for i in range (max(0, x - scale), min(creature.shape[0], x + scale)):
				creature[i][y] = rgb
		else:
			for j in range (max(0, y - scale), min(creature.shape[1], y + scale)):
				creature[x][j] = rgb

	def __point_mutation(self, creature, scale):
		x = np.random.randint(creature.shape[0])
		y = np.random.randint(creature.shape[1])
		rgb = [np.random.randint(0,256), np.random.randint(0,256), np.random.randint(0,256)]
		creature[x][y] = rgb

	def __full_triangle(self, vertices):
	    ab = rg.bresenham_line(vertices[0], vertices[1], endpoint=True)
	    for x in set(ab):
	        yield from rg.bresenham_line(vertices[2], x, endpoint=True)

	def __triangle_mutation(self, creature, scale):
		vertices = [(np.random.randint(creature.shape[0]), np.random.randint(creature.shape[1]))]
		scale = scale + 2
		vertices.append((np.random.randint(vertices[0][0] - scale/2, vertices[0][0] + scale/2), np.random.randint(vertices[0][1] - scale/2, vertices[0][1] + scale/2)))
		vertices.append(
			(np.random.randint(min(vertices[0][0], vertices[1][0]), max(vertices[0][0], vertices[1][0]) + 1), 
			 np.random.randint(min(vertices[0][1], vertices[1][1]), max(vertices[0][1], vertices[1][1]) + 1))
		)
		points = set(self.__full_triangle(vertices))
		rgb = [np.random.randint(0,256), np.random.randint(0,256), np.random.randint(0,256)]
		for point in points:
			if point[0] >= 0 and point[0] < creature.shape[0] and point[1] >= 0 and point[1] < creature.shape[1]:
				creature[point[0]][point[1]] = rgb

	def __circle_mutation(self, creature, scale):
		cy = np.random.randint(creature.shape[0])
		cx = np.random.randint(creature.shape[1])
		r = float(scale)
		y = np.arange(0, creature.shape[0])
		x = np.arange(0, creature.shape[1])
		mask = (x[np.newaxis,:]-cx)**2 + (y[:,np.newaxis]-cy)**2 < r**2
		rgb = [np.random.randint(0,256), np.random.randint(0,256), np.random.randint(0,256)]
		creature[mask] = rgb
