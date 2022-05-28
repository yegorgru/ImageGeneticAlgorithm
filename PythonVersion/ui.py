import PySimpleGUI as sg

class UI:
	def __init__(self, settings):
		self.target_image_name = '-TARGET-IMAGE-'
		self.generated_image_name = '-GENERATED-IMAGE-'
		self.file_path = "-FILE_PATH-"
		self.iteration = "-ITER-"
		self.loss_value = "-LOSS-VALUE"
		self.exit = (sg.WIN_CLOSED, "Exit")
		self.changes_scale = "-CHANGES_SCALE-"
		self.survivors_number = "-SURVIVORS_NUMBER-"
		self.children_number = "-CHILDREN_NUMBER-"
		self.changes_number = "-CHANGES_NUMBER-"
		self.mutation_type = "-COMBO-MUTATION-"
		self.loss_function = "-LOSS-FUNCTION-"
		self.__settings = settings

	def create_window(self):
		settings_col = [
			[sg.Text('Path'), sg.In(size=(25,1), enable_events=True, key=self.file_path), sg.FileBrowse(file_types=(("JPG", "*.jpg"), ("PNG", "*.png"),))],
			[sg.Text('Changes max scale'), sg.Slider(range=(1, 100), default_value=self.__settings.get_changes_scale(), orientation='h', key=self.changes_scale, enable_events=True)],
			[sg.Text('Number of survivors'), sg.Slider(range=(1, 4), default_value=self.__settings.get_survivors_number(), orientation='h', key=self.survivors_number, enable_events=True)],
			[sg.Text('Number of children'), sg.Slider(range=(1, 8), default_value=self.__settings.get_children_number(), orientation='h', key=self.children_number, enable_events=True)],
			[sg.Text('Changes max number'), sg.Slider(range=(1, 50), default_value=self.__settings.get_changes_number(), orientation='h', key=self.changes_number, enable_events=True)],
			[sg.Text('Mutation type'), sg.Combo(values=('Square', 'Line', 'Point', 'Triangle', 'Circle'), default_value='Square', readonly=True, key=self.mutation_type, enable_events=True)],
			[sg.Text('Loss function'), sg.Combo(values=('MSE', 'RMSE', 'MAE', 'Log-Cosh'), default_value='MSE', readonly=True, key=self.loss_function, enable_events=True)],
			[sg.Text('Generation'), sg.Text(size=(40,1), key=self.iteration)],
			[sg.Text('Loss value'), sg.Text(size=(40,1), key=self.loss_value)]
		]
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