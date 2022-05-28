import math
import numpy as np

class LossCounter:
	def get_loss(self, type, target, pred):
		if type == "MSE":
			return self.__mean_squared_error(target, pred)
		if type == "RMSE":
			return self.__root_mean_squared_error(target, pred)
		elif type == "MAE":
			return self.__mean_absolute_error(target, pred)
		elif type == "Log-Cosh":
			return self.__log_cosh_loss(target, pred)

	def __mean_squared_error(self, target, pred):
		diff = (pred - target) ** 2
		mean_diff = diff.mean()
		return mean_diff

	def __mean_absolute_error(self, target, pred):
		diff = np.abs(pred - target)
		mean_diff = diff.mean()
		return mean_diff

	def __root_mean_squared_error(self, target, pred):
		return math.sqrt(self.__mean_squared_error(target, pred))

	def __log_cosh_loss(self, target, pred):
		diff = np.cosh(pred - target)
		mean_diff = diff.mean()
		return math.log(mean_diff)