class Settings:
	def __init__(self):
		self.__changes_scale = 20
		self.__sons_number = 4
		self.__changes_number = 20

	def set_changes_scale(self, value):
		self.__changes_scale = value

	def get_changes_scale(self):
		return self.__changes_scale

	def set_sons_number(self, value):
		self.__sons_number = value

	def get_sons_number(self):
		return self.__sons_number

	def set_changes_number(self, value):
		self.__changes_number = value

	def get_changes_number(self):
		return self.__changes_number