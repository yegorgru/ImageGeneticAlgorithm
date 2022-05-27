import PySimpleGUI as sg

class UI:
	def __init__(self):
		self.target_image_name = '-TARGET-IMAGE-'
		self.generated_image_name = '-GENERATED-IMAGE-'
		self.file_path = "-FILE_PATH-"
		self.iteration = "-ITER-"
		self.exit = (sg.WIN_CLOSED, 'Exit')

	def create_window(self):
		settings_col = [[sg.Text('Path'), sg.In(size=(25,1), enable_events=True, key=self.file_path), sg.FileBrowse(file_types=(("JPG", "*.jpg"), ("PNG", "*.png"),))],
			[sg.Text(size=(40,1), key="-ITER-")]]
		target_image_col = [[sg.Image(key=self.target_image_name)]]
		created_image_col = [[sg.Image(key=self.generated_image_name)]]
		layout = [[sg.Column(settings_col, element_justification='c'), sg.VSeperator(),
				   sg.Column(target_image_col, element_justification='c'), sg.VSeperator(),
				   sg.Column(created_image_col, element_justification='c')]]
		self.__window = sg.Window('Genetic algorithms', layout).Finalize()
		self.__window.Maximize()

	def get_user_input(self, time_interval):
		return self.__window.read(timeout=time_interval)

	def updateData(self, key, value):
		self.__window[key].update(data=value)

	def update(self, key, value):
		self.__window[key].update(value)
	
	def get_width(self):
		return self.__window.size[0]

	def get_height(self):
		return self.__window.size[1]

	def close(self):
		self.__window.close()