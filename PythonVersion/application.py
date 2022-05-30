from ui import UI
from utils import *
from population import Population
from settings import Settings
import time

from numpy import asarray

class Application:
	def __init__(self, control_point_name):
		self.__settings = Settings()
		self.__ui = UI(self.__settings)
		self.__ui.create_window()
		self.__is_running = False
		self.__iter = 0
		self.__target = None
		self.__saved_files_counter = 0
		self.__control_point_name = control_point_name
		self.__next_control_point = 10

	def run(self):
		while True:
		    event, values = self.__ui.get_user_input(10)
		    if event in self.__ui.exit:
		        break
		    elif event == self.__ui.file_path:
		        try:
		            filename = values[event]
		            self.start(filename)
		        except Exception as E:
		            print(f'** Error {E} **')
		            pass
		    elif event == self.__ui.changes_scale:
		    	self.__settings.set_changes_scale(int(values[event]))
		    elif event == self.__ui.survivors_number:
		    	self.__settings.set_survivors_number(int(values[event]))
		    elif event == self.__ui.children_number:
		    	self.__settings.set_children_number(int(values[event]))
		    elif event == self.__ui.changes_number:
		    	self.__settings.set_changes_number(int(values[event]))
		    elif event == self.__ui.mutation_type:
		    	self.__settings.set_mutation_type(values[event])
		    elif event == self.__ui.loss_function:
		    	self.__settings.set_loss_function(values[event])
		    elif event == self.__ui.creation_type:
		    	self.__settings.set_single_parent(values[event])
		    	if self.__settings.is_single_parent():
		    		self.__ui.enable(self.__ui.survivors_number)
		    	else:
		    		self.__settings.set_survivors_number(2)
		    		self.__ui.update(self.__ui.survivors_number, 2)
		    		self.__ui.disable(self.__ui.survivors_number)
		    elif event == self.__ui.stop_resume:
		    	if self.__target is not None:
		    		self.__is_running = not self.__is_running
		    elif event == self.__ui.export:
		    	if self.__target is not None:
		    		self.__saved_files_counter = self.__saved_files_counter + 1
		    		self.export("img" + str(self.__saved_files_counter) + ".jpg")
		    if self.__is_running:
		    	best, loss_value = self.__population.next(self.__target)
		    	self.__ui.updateData(self.__ui.generated_image_name, image_to_bytes(image_from_array(best)))
		    	self.__iter = self.__iter + 1;
		    	self.__ui.update(self.__ui.iteration, self.__iter)
		    	self.__ui.update(self.__ui.loss_value, loss_value)
		    	if self.__iter == self.__next_control_point:
		    		self.control_point()	    		
		self.__ui.close()

	def start(self, filename):
		max_size = self.__ui.get_width()/2.5, self.__ui.get_height() * 0.9
		img = image_from_file(filename, max_size)
		self.__target = asarray(img)
		self.__ui.updateData(self.__ui.target_image_name, image_to_bytes(img))
		self.__population = Population(self.__settings, self.__target.shape, 10)
		self.__is_running = True
		self.__start_time = time_as_int()

	def export(self, filename):
		img = image_from_array(self.__population.get_best_creature())
		img.save(filename)

	def control_point(self):
		if self.__control_point_name is not None:
			self.__next_control_point = self.__next_control_point * 10
			file_object = open(self.__control_point_name + ".txt", 'a+')
			current_time = time_as_int() - self.__start_time
			time_value = '{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
	                                                        (current_time // 100) % 60,
	                                                        current_time % 100)
			file_object.write(time_value + "\n")
			self.export(self.__control_point_name + str(self.__iter) + '.jpg')

