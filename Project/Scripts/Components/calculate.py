import math

class Calculate:
	# def __init__(self):

	
	# # valueX
	# def getValueX(self):
	#     return self.valueX
	
	# def setValueX(self, x):
	#     self.valueX = x
	
	# # valueY
	# def getValueY(self):
	#     return self.valueY
	# def setValueY(self, y):
	#     self.valueY = y
	
	# # result
	# def getResult(self):
	#     return self.result
	# def setResult(self, result):
	#     self.result = result

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

	# @classmethod
	# def findOperation(self,operation,x,y=0):
	#     self.valueX(x)
	#     self.valueY(y)
	#     result = 0
	#     if operation == 'add':
	#         result = self.add()
	#     elif operation == 'subtract':
	#         result = self.subtract()
	#     elif operation == 'multiply':
	#         result = self.multiply()
	#     elif operation == 'divide':
	#         result = self.divide()
	#     # what is going to be the keyword for square root again?
	#     elif operation == 'square root':
	#         result = self.squareRoot()
	#     return result

# idk which functions we want returning results, right now its pretty redundant
# im setting our class variables in each function yet also returning