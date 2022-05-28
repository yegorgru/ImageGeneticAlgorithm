class Settings:
	def __init__(self):
		self.__changes_scale = 20
		self.__survivors_number = 2
		self.__children_number = 4
		self.__changes_number = 20
		self.__mutation_type = "Square"
		self.__loss_function = "MSE"

	def set_changes_scale(self, value):
		self.__changes_scale = value

	def get_changes_scale(self):
		return self.__changes_scale

	def set_survivors_number(self, value):
		self.__survivors_number = value

	def get_survivors_number(self):
		return self.__survivors_number

	def set_children_number(self, value):
		self.__children_number = value

	def get_children_number(self):
		return self.__children_number

	def set_changes_number(self, value):
		self.__changes_number = value

	def get_changes_number(self):
		return self.__changes_number

	def set_mutation_type(self, value):
		self.__mutation_type = value

	def get_mutation_type(self):
		return self.__mutation_type

	def set_loss_function(self, value):
		self.__loss_function = value

	def get_loss_function(self):
		return self.__loss_function
