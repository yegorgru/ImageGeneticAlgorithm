from ui import UI
from image_loader import *
from population import Population

from numpy import asarray

class Application:
	def __init__(self):
		self.__ui = UI()
		self.__ui.create_window()
		self.__is_running = False
		self.__iter = 0

	def run(self):
		while True:
		    event, values = self.__ui.get_user_input(10)
		    if event in self.__ui.exit:
		        break
		    if event == self.__ui.file_path:
		        try:
		            filename = values[event]
		            self.start(filename)
		        except Exception as E:
		            print(f'** Error {E} **')
		            pass
		    if self.__is_running:
		    	self.__population.next(self.__target)
		    	self.__ui.updateData(self.__ui.generated_image_name, image_to_bytes(image_from_array(self.__population.get_best())))
		    	self.__iter = self.__iter + 1;
		    	self.__ui.update(self.__ui.iteration, self.__iter)
		self.__ui.close()

	def start(self, filename):
		size = self.__ui.get_width()/2.5, self.__ui.get_height()/2.5
		img = image_from_file(filename, size)
		self.__target = asarray(img)
		self.__ui.updateData(self.__ui.target_image_name, image_to_bytes(img))
		self.__population = Population(self.__target.shape, 10)
		self.__is_running = True