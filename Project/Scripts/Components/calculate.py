import math

class Calculate:
	def add(self, val1, val2):
		try:
			return val1 + val2
		except TypeError:
			return None

	def subtract(self, val1, val2):
		try:
			return val2 - val1
		except TypeError:
			return None

	def multiply(self, val1, val2):
		try:
			return val1 * val2
		except TypeError:
			return None

	def divide(self, val1, val2):
		try:
			result =  val1 / val2
		except ZeroDivisionError:
			return None	
		except TypeError:
			return None
		finally:
			if ((float(result)).is_integer()):
				return int(float(result))
			return result

	def squareRoot(self, val1):
		if val1 < 0:
			print('ERROR: CANNOT SQUARE ROOT A NEGATIVE VALUE')
			return None
		else:
			return math.sqrt(val1)