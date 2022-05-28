from ui import UI
from image_loader import *
from population import Population
from settings import Settings

from numpy import asarray

class Application:
	def __init__(self):
		self.__settings = Settings()
		self.__ui = UI(self.__settings)
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
		    if event == self.__ui.changes_scale:
		    	self.__settings.set_changes_scale(int(values[event]))
		    if event == self.__ui.sons_number:
		    	self.__settings.set_sons_number(int(values[event]))
		    if event == self.__ui.changes_number:
		    	self.__settings.set_changes_number(int(values[event]))
		    if event == self.__ui.mutation_type:
		    	self.__settings.set_mutation_type(values[event])
		    if event == self.__ui.loss_function:
		    	self.__settings.set_loss_function(values[event])
		    if self.__is_running:
		    	best, loss_value = self.__population.next(self.__target)
		    	self.__ui.updateData(self.__ui.generated_image_name, image_to_bytes(image_from_array(best)))
		    	self.__iter = self.__iter + 1;
		    	self.__ui.update(self.__ui.iteration, self.__iter)
		    	self.__ui.update(self.__ui.loss_value, loss_value)
		self.__ui.close()

	def start(self, filename):
		size = self.__ui.get_width()/2.5, self.__ui.get_height()/2.5
		img = image_from_file(filename, size)
		self.__target = asarray(img)
		self.__ui.updateData(self.__ui.target_image_name, image_to_bytes(img))
		self.__population = Population(self.__settings, self.__target.shape, 10)
		self.__is_running = True